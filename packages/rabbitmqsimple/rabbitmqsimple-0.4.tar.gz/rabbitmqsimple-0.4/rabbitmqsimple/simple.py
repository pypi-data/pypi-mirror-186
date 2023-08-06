from rabbitpy import Connection
from rabbitpy import Exchange
from rabbitpy import Queue
from rabbitpy import Message
import os

from rabbitmqsimple.consumer import RMQConsumer
from rabbitmqsimple.exception import RabbitMQSimpleException


class RMQSimple:
    """
    This class simplified the configuration of RabbitMQ in multi tenant environment.
    It provides methods for managing Exchanges, Queues, Messages, Consumers.
    """
    MQ_USERNAME = os.getenv("MQ_USERNAME")
    MQ_PASSWORD = os.getenv("MQ_PASSWORD")
    MQ_HOST = os.getenv("MQ_HOST")
    MQ_PORT = os.getenv("MQ_PORT")
    MQ_ENV = os.getenv("MQ_ENV")
    SEPARATOR = "/"


    def __init__(self, tenant_id):
        try:
            self.uri = "amqps://" + RMQSimple.MQ_USERNAME + ":" + RMQSimple.MQ_PASSWORD + "@" \
                       + RMQSimple.MQ_HOST + ":" + RMQSimple.MQ_PORT
            self.conn = Connection(self.uri)
            self.channel = self.conn.channel()
            self.directExchange = None
            self.queues = []
            self.tenant_id = tenant_id
        except Exception as e:
            print('Error in connecting to RabbitMQ. Please check environment varaibles!!!!')
            raise RabbitMQSimpleException(RabbitMQSimpleException.CONNECTION_ERROR)

    def createExchange(self, tenant_id, ex_type="direct"):
        """
        This method create an exchange on RabbitMQ server. By default, it creates Direct Exchange.
        Other type of exchanges can be created by passing ex_type parameter.

        :param tenant_id: ID of the tenant
        :param ex_type: Type of exchange, default is direct
        :return: rabbitpy.Exchange Object
        """
        exchange_name = tenant_id + "/" + ex_type
        print('Creating Exchange of type {0} with name as {1} '.format(ex_type, exchange_name))
        obj = None
        try:
            if ex_type == "direct":
                self.directExchange = Exchange(self.channel, exchange_name, exchange_type=ex_type, durable=True,
                                               auto_delete=False)
                self.directExchange.declare()
                obj = self.directExchange
            print('exit from Exchange', self.directExchange)
            return obj
        except Exception as e:
            print("Error in creating Exchange")
            raise RabbitMQSimpleException(RabbitMQSimpleException.CREATE_EXCHANGE_ERROR)
        finally:
            return obj

    def getExchange(self, ex_type="direct"):
        """
        This method return the instance of an exchange

        :param ex_type: Type of exchange instance want to fetch
        :return: rabbitpy.Exchange Object
        """
        if ex_type == "direct":
            return self.directExchange
        else:
            return None

    def createQueue(self, tenant_id, name, exchange, routing_key=None):
        """
        This method create a Queue on RabbitMQ server. It also binds it with the exchange
        passed as parameter. By default, the routing key will be used as queue name. If you want to have a different
        routing key, then pass parameter routing_key with required value.

        :param tenant_id: ID of the tenant
        :param name: Name of the queue
        :param exchange: Exchange object to bind Queue
        :param routing_key: Routing Key to bind Queue
        :return: rabbitpy.Queue
        """
        try:
            queue_name = self.getQueueName(tenant_id, name) #tenant_id + "/" + name
            queue = Queue(self.channel, queue_name, durable=False,
                          max_length=None, message_ttl=None, expires=None,
                          dead_letter_exchange=None, dead_letter_routing_key=None)
            t = queue.declare()
            self.bindQueue(queue, exchange, routing_key=queue_name)

            q = (queue_name, queue)
            self.queues.append(q)
            return t
        except Exception as e:
            print("Error in creating and declaring Queue")
            raise RabbitMQSimpleException(RabbitMQSimpleException.CREATE_QUEUE_ERROR)

    def bindQueue(self, queue, exchange, routing_key=None):
        """
        This method bind a Queue to an exchange. It will be call internally from createQueue method.

        :param queue: Queue object for binding
        :param exchange: Exchange object to bind Queue
        :param routing_key: Routing Key to bind Queue
        :return: None
        """
        try:
            queue.bind(exchange, routing_key)
        except Exception as e:
            print("Error in binding Queue")
            raise RabbitMQSimpleException(RabbitMQSimpleException.BIND_QUEUE_ERROR)

    def unbindQueue(self, queue, exchange: Exchange):
        """
          This method unbind a Queue to an exchange.

          :param queue: Queue object for binding
          :param exchange: Exchange object to bind Queue
          :return: None
        """
        try:
            queue.unbind(exchange)
        except Exception as e:
            print("Error in unbinding Queue")
            raise RabbitMQSimpleException(RabbitMQSimpleException.UNBIND_QUEUE_ERROR)

    def createMessage(self, value, props=None):
        """
        This method is used to create a message.

        :param value: body of the message
        :param props: message properties, optional
        :return: rabbitpy.Message
        """
        try:
            msg = Message(self.channel, body_value=value, properties=props, opinionated=True)
            return msg
        except Exception as e:
            print("Error in creating message")
            raise RabbitMQSimpleException(RabbitMQSimpleException.CREATE_MESSAGE_ERROR)

    def getQueueName(self, tenant_id, name: str) -> str:
        """
        This method encapsulate the logic for creating queue name. The name parameter will be prefixed with the tenant id,
        separated by '/' (default)

        :param tenant_id: ID of the tenant
        :param name: name of the queue
        :return: String, queue name with tenant as prefix
        """
        return tenant_id + self.SEPARATOR + name

    def getQueue(self, queue_name: str):
        """
        This method will return a Queue instance corresponding to the name passed in the parameter queue_name.

        :param queue_name: name of the queue
        :return: rabbitpy.Queue
        """
        try:
            queue = [tup for tup in self.queues if tup[0] == queue_name]
            obj = queue[0][1]
            print('Queue Object', obj)
            return obj
        except Exception as e:
            print("Error in fetching queue from list", e)
            raise RabbitMQSimpleException(RabbitMQSimpleException.FETCH_QUEUE_ERROR)


    def registerConsumer(self, queue_name: str, consumer: RMQConsumer):
        """
        This method register a consumer instance and will start listening to the Queue for message. It will continue to
        read messages until it is interrupted by pressing Ctrl+C.

        :param queue_name: Name of the queue
        :param consumer: An object of RMQConsumer
        :return: None
        """
        queue = self.getQueue(queue_name)
        try:
            # Consume the message
            for message in queue:
                print('consuming message',message.body)
                consumer.processMessage(message)
                message.ack()
        except KeyboardInterrupt:
            print ('Exited consumer')
        except Exception as e:
            print("Error in adding consumer ", e)
            raise RabbitMQSimpleException(RabbitMQSimpleException.CREATE_CONSUMER_ERROR)

    def getConsumerCount(self, queue_name: str) -> int:
        """
        This method will return the number of consumer bind with the Queue.

        :param queue_name: The name of queue without tenant id
        :return: int, count of consumer
        """
        try:
            queue_name = self.getQueueName(self.tenant_id, queue_name)
            queue = self.getQueue(queue_name)
            count = queue.declare()[1]
            print('Total consumer on queue ', queue_name, count)
            return count
        except Exception as e:
            print("Error in fetching consumer count ", e)
            raise RabbitMQSimpleException(RabbitMQSimpleException.FETCH_CONSUMER_COUNT_ERROR)

    def getMessageCount(self, queue_name):
        """
        This method will return the number of unread message in the Queue.

        :param queue_name: The name of queue without tenant id
        :return: int, count of unread messages
        """
        try:
            queue_name = self.getQueueName(self.tenant_id, queue_name)
            queue = self.getQueue(queue_name)
            count = queue.declare()[0]
            print('Total message count', queue_name, count)
            return count
        except Exception as e:
            print("Error in fetching message count ", e)
            raise RabbitMQSimpleException(RabbitMQSimpleException.FETCH_MESSAGE_COUNT_ERROR)


    def stopConsuming(self, queue_name):
        queue = [tup for tup in self.queues if tup[0] == queue_name]
        obj = queue[0][1]
        obj.stop_consuming()
        return obj

    def close(self):
        self.channel.close()
        self.conn.close()
