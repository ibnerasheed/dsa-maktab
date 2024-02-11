from dsa.common.node import Node
from dsa.common.exceptions import UnderflowException

class DynamicQueue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__size = 0
          
    def empty(self):
        return self.__rear is None    
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.empty():
            self.__front = new_node
        else:
            self.__rear.next = new_node
        
        self.__rear = new_node 
        self.__size = self.__size + 1
    
    def dequeue(self):
        if self.empty():
            raise UnderflowException('Queue Underflow')
        data = self.__front.data
        self.__front = self.__front.next
        return data
        


    def __len__(self):
        return self.__size
        
    def __str__(self):
        temp = ""
        temp_ref = self.__front
        for _ in range(0,self.__size):
            temp = f"{temp}{temp_ref.data}, "
            temp_ref = temp_ref.next
            
        

        return f"[{temp[:-2]}]"
