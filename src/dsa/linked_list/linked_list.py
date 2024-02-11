from dsa.common.node import Node


class LinkedList:
    def __init__(self):
        self.__head = None
        

    def empty(self):
        return not self.__head

    def add_at_start(self, data):
        new_node = Node(data, self.__head)
        self.__head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.empty():
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    
    """Refavtor the below code"""
    def delete(self, data):
        temp = self.__head
        temp2 = None
        while temp is not None:
            if temp.data == data:
                if temp2 is None:
                    self.__head = temp.next
                else:
                    temp2.next = temp.next
                return temp.data
            else:
                temp2 = temp
                temp = temp.next
        raise ValueError(f"Data: {data} not found")        

    def search(self, data):
        temp = self.__head
        position = 0

        while temp is not None:
            position += 1
            if temp.data == data:
                return position
            temp = temp.next
        raise ValueError(f"Data: {data} not found")

    def add_at_location(self, location, data):
        new_node = Node(data)
        if location == 1:
            new_node.next = self.__head
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
        
    def reverse(self):
        if self.__head is None or self.__head.next is None:
            return
        ref = self.__head.next
        ref_behind = self.__head
        ref_behind.next = None
        while ref is not None:
            temp = ref.next
            ref.next = ref_behind
            ref_behind = ref
            ref = temp
        self.__head = ref_behind              

    
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

    


