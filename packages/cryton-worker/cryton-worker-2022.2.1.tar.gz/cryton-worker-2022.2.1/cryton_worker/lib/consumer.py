from click import echo
import amqpstorm
import json
import time
from typing import List
from multiprocessing import Lock
from threading import Thread

from cryton_worker.lib import task
from cryton_worker.lib.util import logger, util


class ChannelConsumer:
    def __init__(self, identifier: int, connection: amqpstorm.Connection, queues: dict):
        self._id = identifier
        self._channel = connection.channel()

        self._channel.basic.qos(1)
        for queue, callback in queues.items():  # Consume on each queue.
            self._channel.queue.declare(queue)
            self._channel.basic.consume(callback, queue)

    def start(self):
        logger.logger.debug("Channel consumer started.", id=self._id)
        while not self._channel.is_closed:
            try:
                self._channel.start_consuming()

            except amqpstorm.AMQPConnectionError as ex:
                logger.logger.debug("Channel consumer encountered a connection error.", id=self._id, error=str(ex))
                break

            except Exception as ex:  # If any uncaught exception occurs, channel consumer will still work
                logger.logger.warning("Channel consumer encountered an error.", id=self._id, error=str(ex))

        logger.logger.debug("Channel consumer stopped.", id=self._id)


class Consumer:
    def __init__(self, main_queue: util.ManagerPriorityQueue, rabbit_host: str, rabbit_port: int, rabbit_username: str,
                 rabbit_password: str, worker_name: str, consumer_count: int, max_retries: int, persistent: bool):
        """
        Consumer takes care of the connection between Worker and RabbitMQ server and launching callbacks for the
        defined queues.
        Update Queues here and add _callback_queue method to this Class.
        :param main_queue: Worker's queue for internal request processing
        :param rabbit_host: Rabbit's server port
        :param rabbit_port: Rabbit's server host
        :param rabbit_username: Rabbit's username
        :param rabbit_password: Rabbit's password
        :param worker_name: Worker name (prefix) for queues
        :param consumer_count: How many consumers to use for queues (higher == faster, but heavier processor usage)
        :param max_retries: How many times to try to connect
        :param persistent: Keep Worker alive and keep on trying forever (if True)
        """
        attack_q = f"cryton_worker.{worker_name}.attack.request"
        agent_q = f"cryton_worker.{worker_name}.agent.request"
        control_q = f"cryton_worker.{worker_name}.control.request"
        self._queues = {attack_q: self._callback_attack, control_q: self._callback_control, 
                        agent_q: self._callback_agent}

        self._hostname = rabbit_host
        self._port = rabbit_port
        self._username = rabbit_username
        self._password = rabbit_password
        self._max_retries = max_retries
        self._persistent = persistent
        self._main_queue = main_queue
        self._channel_consumer_count = consumer_count if consumer_count > 0 else 1
        self._stopped = False
        self._connection: amqpstorm.Connection or None = None
        self._tasks: List[task.Task] = []
        self._tasks_lock = Lock()  # Lock to prevent modifying, while performing time-consuming actions.

    def __str__(self) -> str:
        return f"{self._username}@{self._hostname}:{self._port}"

    def is_running(self) -> bool:
        return not self._stopped

    # TODO: should run in a Process
    def start(self) -> None:  # TODO: resolve the KeyboardError to prevent t_consumer raise Exception on channel fail
        """
        Establish connection, start channel consumers in thread and keep self alive.
        :return: None
        """
        logger.logger.debug("Consumer started.", hostname=self._hostname, port=self._port, username=self._username,
                            queues=self._queues, max_retries=self._max_retries, persistent=self._persistent,
                            channel_consumer_count=self._channel_consumer_count)
        self._stopped = False

        while self.is_running():  # Keep self and connection alive and check for stop.
            try:
                if self._update_connection():
                    self._start_channel_consumers()
                time.sleep(5)

            except amqpstorm.AMQPConnectionError as ex:
                if self._persistent:
                    logger.logger.debug("Ignoring connection error due to persistent mode.", error=str(ex))
                    echo("Due to persistent mode, Worker will try to reconnect util manual shutdown.")
                    continue
                self._stopped = True
                echo("Stopping due to connection loss..")

    def stop(self) -> None:
        """
        Stop Consumer (self). Wait for running Tasks (optionally kill them), close connection and its channels.
        :return: None
        """
        logger.logger.debug("Stopping Consumer.", hostname=self._hostname, port=self._port, username=self._username)
        self._stopped = True

        try:  # Wait for Tasks to finish.
            logger.logger.debug("Waiting for unfinished Tasks.")
            echo("Waiting for running modules to finish.. press CTRL + C to kill them.")
            with self._tasks_lock:
                while len(self._tasks) > 0:
                    task_obj = self._tasks.pop(-1)
                    try:
                        task_obj.join()
                    except KeyboardInterrupt:
                        task_obj.kill()
                        task_obj.join()
                        raise KeyboardInterrupt

        except KeyboardInterrupt:  # Kill remaining Tasks.
            logger.logger.debug("Killing unfinished Tasks.")
            echo("Forcefully killing running modules..")
            with self._tasks_lock:
                while len(self._tasks) > 0:
                    task_obj = self._tasks.pop(-1)
                    task_obj.kill()
                    task_obj.join()

        if self._connection is not None and self._connection.is_open:  # Close connection and its channels.
            logger.logger.debug("Closing channels.")
            echo("Closing connection and it's channels..")
            for channel in list(self._connection.channels.values()):
                channel.close()
            logger.logger.debug("Closing connection.")
            self._connection.close()

        logger.logger.debug("Consumer stopped.", hostname=self._hostname, port=self._port, username=self._username)

    def _update_connection(self) -> bool:
        """
        Check existing connection for errors and optionally reconnect.
        Debug logs aren't present since it creates not necessary information.
        :return: True if connection was updated
        """
        try:  # If connection is missing or there is some other problem, raise exception.
            if self._connection is None:
                raise amqpstorm.AMQPConnectionError("Connection does not exist.")

            if not self._connection.is_open:
                raise amqpstorm.AMQPConnectionError("Connection is closed.")

            self._connection.check_for_errors()
            return False

        except amqpstorm.AMQPError as ex:  # Try to establish connection or error.
            echo(f"{str(ex)} Retrying..")
            logger.logger.warning("Connection lost.", error=str(ex))
            self._create_connection()

        return True

    def _start_channel_consumers(self) -> None:
        """
        Start consumers in thread.
        :return: None
        """
        logger.logger.debug("Starting channel consumers", channel_consumer_count=self._channel_consumer_count)
        for i in range(self._channel_consumer_count):
            channel_consumer = ChannelConsumer(i + 1, self._connection, self._queues)
            thread = Thread(target=channel_consumer.start, name=f"Thread-{i}-consumer")
            thread.start()

    def _callback_attack(self, message: amqpstorm.Message) -> None:
        """
        Create new AttackTask and save it.
        :param message: Received RabbitMQ Message
        :return: None
        """
        logger.logger.debug("Calling attack callback.", correlation_id=message.correlation_id,
                            message_body=message.body)
        task_obj = task.AttackTask(message, self._main_queue)
        task_obj.start()
        with self._tasks_lock:
            self._tasks.append(task_obj)

    def _callback_agent(self, message: amqpstorm.Message) -> None:
        """
        Create new AgentTask and save it.
        :param message: Received RabbitMQ Message
        :return: None
        """
        logger.logger.debug("Calling agent callback.", correlation_id=message.correlation_id,
                            message_body=message.body)
        task_obj = task.AgentTask(message, self._main_queue)
        task_obj.start()
        with self._tasks_lock:
            self._tasks.append(task_obj)

    def _callback_control(self, message: amqpstorm.Message) -> None:
        """
        Create new ControlTask and save it.
        :param message: Received RabbitMQ Message
        :return: None
        """
        logger.logger.debug("Calling control callback.", correlation_id=message.correlation_id,
                            message_body=message.body)
        task_obj = task.ControlTask(message, self._main_queue)
        task_obj.start()
        with self._tasks_lock:
            self._tasks.append(task_obj)

    def _create_connection(self) -> None:
        """
        Try to create a connection to a RabbitMQ server.
        :raises: amqpstorm.AMQPConnectionError if connection can't be established
        :return: None
        """
        logger.logger.debug("Establishing connection.")
        for attempt in range(self._max_retries):
            if not self.is_running():
                return

            try:  # Create connection.
                self._connection = amqpstorm.Connection(self._hostname, self._username, self._password, self._port)
                logger.logger.debug("Connection established.")
                echo("Connection to RabbitMQ server established.")
                echo("[*] Waiting for messages.")
                return

            except amqpstorm.AMQPError as ex:
                logger.logger.warning("Connection couldn't be established.", error=str(ex))
                echo(f"Connection couldn't be established. (attempt {attempt + 1}/{self._max_retries})")
                if attempt + 1 < self._max_retries:
                    time.sleep(min(attempt + 1 * 2, 30))

        logger.logger.error("Max number of retries reached.")
        raise amqpstorm.AMQPConnectionError("Max number of retries reached.")

    def send_message(self, queue: str, message_body: dict, message_properties: dict) -> None:
        """
        Open a new channel and send a custom message.
        :param queue: Target queue (message receiver)
        :param message_body: Message content
        :param message_properties: Message properties (options)
        :return: None
        """
        logger.logger.debug("Sending message.", queue=queue, message=message_body, properties=message_properties)
        channel = self._connection.channel()
        channel.queue.declare(queue)

        message_body = json.dumps(message_body)
        message = amqpstorm.Message.create(channel, message_body, message_properties)
        # TODO: publish can raise an error when a message is not acked, it also freezes until it raises and error due
        #  to a timeout (base rabbit message ack timeout)
        message.publish(queue)
        channel.close()
        logger.logger.debug("Message sent.", queue=queue, message=message_body, properties=message_properties)

    def pop_task(self, correlation_id) -> task.Task or None:
        """
        Find a Task using correlation_id and remove it from tasks.
        :param correlation_id: Task's correlation_id
        :return: Task matching correlation_id, or None if none matched
        """
        logger.logger.debug("Popping (searching) Task using correlation_id.", correlation_id=correlation_id)
        with self._tasks_lock:
            for i in range(len(self._tasks)):
                if self._tasks[i].correlation_id == correlation_id:
                    logger.logger.debug("Task popping (search) succeeded.", correlation_id=correlation_id)
                    return self._tasks.pop(i)

        logger.logger.debug("Task popping (search) failed.", correlation_id=correlation_id)
