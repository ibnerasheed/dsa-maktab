from dsa.common.exceptions import OverflowException,UnderflowException

class FixedSizeStack(object):
    def __init__(self, size):
        self._data = [None]*size
        self._top = -1
        
    
    def empty(self):
        return self._top == -1
           
    def push(self,data):
        stackIsFull = (self._top == (len(self._data)-1))
        if stackIsFull:
            raise OverflowException('Stack Overflow')
        
        self._top = self._top + 1
        self._data[self._top] = data
        
    def peek(self): 
        stackIsEmpty = (self._top == -1)
        if stackIsEmpty:
            raise UnderflowException
        return self._data[self._top]
    
    def pop(self):
        stackIsEmpty = (self._top == -1)
        if stackIsEmpty:
            raise UnderflowException
        poppedElement = self._data[self._top]
        self._top -= 1
        return poppedElement

    def __len__(self):
        return self._top+1 




