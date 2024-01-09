from dsa.common.node import DoubleyNode

class DoubleyLinkedList:
    def __init__(self):
        self.__head = None

    
    def empty(self):
        return not self.__head
    
    def add_at_start(self, data):
        new_node = DoubleyNode(data,None, self.__head)
        if not self.empty():
            self.__head.previous = new_node
            self.__head = new_node  
        self.__head = new_node
    
    def append(self, data):
        new_node = DoubleyNode(data)
        if self.empty():
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.previous = temp
        

    def add_at_location(self, location, data):
        new_node = DoubleyNode(data)
        if location == 1:
            new_node.next = self.__head
            self.__head.previous = new_node
            self.__head = new_node     
        else:  
            temp = self.__head     
            count = 1
            while count < (location-1) and temp is not None:
                count+=1
                temp = temp.next 
            
            if temp is None:
                raise ValueError(f"Location: {location} not found") 
            
            new_node.next = temp.next
            temp.next = new_node
            new_node.previous = temp
            temp.next.previous= new_node

    def search(self, data):
        temp = self.__head
        position = 0

        while temp is not None:
            position += 1
            if temp.data == data:
                return position
            temp = temp.next
        raise ValueError(f"Data: {data} not found")
    
    def delete(self, data):
        temp = self.__head
        while temp is not None:
            if temp.data == data:
                if temp.previous is None:
                    self.__head = temp.next
                    temp.previous = None
                else:    
                    temp.previous.next = temp.next
                return temp.data
            temp = temp.next

        raise ValueError(f"Data: {data} not found")  

    def __str__(self):
        temp = ""
        temp_ref = self.__head
        while temp_ref is not None:
            temp = f"{temp}{temp_ref.data}, "
            temp_ref = temp_ref.next

        return f"[{temp[:-2]}]"

    def __len__(self):
        count = 0
        temp = self.__head
        while temp is not None:
            count += 1
            temp = temp.next
        return count



            
    