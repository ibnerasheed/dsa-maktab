class OverflowException(Exception):
    def getMessage(self):
        return "Stack Overflow"

class UnderflowException(Exception):
    def getMessage(self):
        return "Stack Underflow"
    
