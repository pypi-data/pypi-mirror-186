

class RabbitMQSimpleException(Exception):
    """
    This class define Error codes and messages.
    """
    SPLITTER = "-@-"

    GENERIC_ERROR = "1000" + SPLITTER + "Encounter some internal error. Please contact administrator."
    CONNECTION_ERROR = "1002" + SPLITTER + "Facing issues in connection to RabbitMQ server"
    CREATE_EXCHANGE_ERROR = "1003" + SPLITTER + "Facing issues in creating Exchange"
    CREATE_QUEUE_ERROR = "1004" + SPLITTER + "Facing issues in creating Queue"
    BIND_QUEUE_ERROR = "1005" + SPLITTER + "Facing issues in binding Queue"
    UNBIND_QUEUE_ERROR = "1006" + SPLITTER + "Facing issues in unbinding Queue"
    CREATE_MESSAGE_ERROR = "1007" + SPLITTER + "Facing issues in creating message"
    FETCH_QUEUE_ERROR = "1008" + SPLITTER + "Facing issues in fetching Queue"
    CREATE_CONSUMER_ERROR = "1009" + SPLITTER + "Facing issues in creating consumer"
    FETCH_CONSUMER_COUNT_ERROR = "1010" + SPLITTER + "Facing issues in fetching consumer count"
    FETCH_MESSAGE_COUNT_ERROR = "1010" + SPLITTER + "Facing issues in fetching message count"

    def __init__(self, error_code, exp=""):
        self.error_code = error_code
        self.root_exception = exp

    def getErrorMsg(self):
        Code, Message = "", ""
        try:
            if self.error_code:
                lst = self.error_code.split(RabbitMQSimpleException.SPLITTER)
                Code, Message = lst[0], lst[1]
            return Code, Message
        except Exception as e:
            print('Error in getting error code and message', e)
            return Code, Message
