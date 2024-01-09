from dsa.common.node import Node
from dsa.common.exceptions import UnderflowException

class DynamicStack:
    def __init__(self):
        self.__head = None

    def empty(self):
        return self.__head is None

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.__head
        self.__head = newNode

    def pop(self):
        if self.empty():
            raise UnderflowException
        poppedData = self.__head.data
        self.__head = self.__head.next
        return poppedData
           

    def peek(self):
        return self.__head.data
    
    def __len__(self):
        count = 0
        temp = self.__head
        while temp is not None:
            count+=1
            temp = temp.next
        return count 

     
        
