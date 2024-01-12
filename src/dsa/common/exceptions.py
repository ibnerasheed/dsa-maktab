class OverflowException(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def getMessage(self):
        return self.__msg

class UnderflowException(Exception):
    def __init__(self, msg):
        self.__msg = msg
    
    def getMessage(self):
        return self.__msg
    
