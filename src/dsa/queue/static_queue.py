from dsa.common.exceptions import OverflowException,UnderflowException

class FixedSizeQueue:
    def __init__(self, capacity):
        self.__data = [None]*capacity
        self.__rear = -1
        self.__front = -1
        self.__capacity = capacity
        self.__size = 0

    def empty(self):
        return self.__size == 0
    
    def enqueue(self, data):
        if self.__size == self.__capacity:
            raise OverflowException('Queue Overflow')
        
        if self.empty(): 
            self.__front = (self.__front + 1) % self.__capacity
        
        self.__rear = (self.__rear + 1) % self.__capacity
        self.__data[self.__rear] = data 
        self.__size+=1    

        
            

    def dequeue(self):
        if self.empty():
            raise UnderflowException('Queue Underflow')
        
        dequeued_element = self.__data[self.__front]
        if self.__front == self.__rear:  
            self.__front = self.__rear = -1
        else:      
            self.__front = (self.__front + 1) % self.__capacity
            
        self.__size-=1    
        return dequeued_element
   
   
    def __str__(self) -> str:
        temp = ""
        temp_front = self.__front
        for _ in range(self.__size):
            temp = f"{temp}{self.__data[temp_front]}, "
            temp_front = (temp_front + 1) % self.__capacity
        return f"[{temp[:-2]}]"    