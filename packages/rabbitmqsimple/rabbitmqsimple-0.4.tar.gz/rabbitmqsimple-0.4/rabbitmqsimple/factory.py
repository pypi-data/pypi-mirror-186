import rabbitmqsimple.simple
from rabbitmqsimple.exception import RabbitMQSimpleException
from rabbitmqsimple.simple import RMQSimple


class RMQFactory:
    """
    This class act as a factory for RMQSimple objects. It will create instance of RMQSimple class for each tenant.
    """
    rmqsimpleList = []

    @classmethod
    def getInstance(cls, tenant_id) -> RMQSimple:
        """
        This method will return an instance of RMQSimple class based on the tenant value as in the parameter.

        :param tenant_id: ID for the tenant
        :return: rabbitmqsimple.simple.RMQSimple
        """
        try:
            filteredList = [tup for tup in RMQFactory.rmqsimpleList if tup[0] == tenant_id]
            if len(filteredList) == 0:
                obj = RMQFactory.createRMQSimple(tenant_id)
            else:
                obj = filteredList[0][1]
            print('object', obj)
            return obj
        except RabbitMQSimpleException as rmqException:
            print("Error in fetching Instance for tenant_id ", tenant_id)
            raise rmqException
        except Exception as e:
            raise RabbitMQSimpleException(RabbitMQSimpleException.GENERIC_ERROR)

    @classmethod
    def createRMQSimple(cls, tenant_id):
        try:
            obj = RMQSimple(tenant_id)
            t = (tenant_id, obj)
            RMQFactory.rmqsimpleList.append(t)
            return obj
        except RabbitMQSimpleException as rmqException:
            print("Error in connecting to RabbitMQ")
            raise rmqException
        except Exception as e:
            raise RabbitMQSimpleException(RabbitMQSimpleException.GENERIC_ERROR)

    @classmethod
    def register(cls, tenant_id, queues, ex_type="direct"):
        """
        This method will configure RabbitMQ Server with and exchange and queues. You must call this method from your app
        to create and exchange of desired type and queues. It will create an exchange, queues and bind queues to the exchange.
        If you want to create multiple exchange, then you need to call this method separately for each exchange.

        :param tenant_id: Id of the tenant
        :param queues: List of a Tuples -> (queue_name, routing_key)
        :param ex_type: type of exchange, default is "direct"
        :return: None
        """
        try:
            instance = RMQFactory.getInstance(tenant_id)
            ex = instance.createExchange(tenant_id=tenant_id, ex_type=ex_type)
            for q in queues:
                instance.createQueue(tenant_id=tenant_id, name=q[0], exchange=ex, routing_key=q[1])
        except RabbitMQSimpleException as rmqException:
            print("Error in creating exchange", rmqException.getErrorMsg())
            raise RabbitMQSimpleException(RabbitMQSimpleException.CREATE_QUEUE_ERROR)
        except Exception as e:
            print("Error in creating exchange", e)
            raise RabbitMQSimpleException(RabbitMQSimpleException.GENERIC_ERROR)
        finally:
            return instance
