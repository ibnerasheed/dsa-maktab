class FixedSizeQueue:
    def __init__(self, size):
        self.__data = [None]*size
        self.__rear = -1
        self.__front = -1

    def empty(self):
        return self.__rear and self.__front == -1 
    
    def enqueue(self, data):
        if self.empty():
            self.__rear+=1
            self.__front+=1
            self.__data[self.__front] = data
        else:    
            self.__rear = self.__rear + 1
            self.__data[self.__rear] = data

    def dequeue(self):
        pass
        
   
    def __str__(self) -> str:
        temp = ""
        for index in range(self.__rear + 1):
            temp = f"{temp}{self.__data[index]}, "
            index+=1
        return f"[{temp[:-2]}]"    