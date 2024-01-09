from dsa.common.node import Node


class CircularLinkedList:
    def __init__(self):
        self.__tail = None
        self.__size = 0

    def empty(self):
        return self.__tail is None

    def add_at_start(self, data):
        new_node = Node(data)
        if self.empty():
            self.__tail = new_node
            new_node.next = new_node
            self.__size+=1 
        else:
            new_node.next = self.__tail.next
            self.__tail.next = new_node
            self.__size+=1
        
    def __len__(self):
        return self.__size

    def __str__(self):
        temp = ""
        head = None
        if not self.empty():
            head = self.__tail.next
        temp_ref = head
        while head and True:
            temp = f"{temp}{temp_ref.data}, "
            temp_ref = temp_ref.next
            if temp_ref is head:
                break

        return f"[{temp[:-2]}]"