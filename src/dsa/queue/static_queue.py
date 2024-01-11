class FixedSizeQueue:
    def __init__(self, size):
        self.__data = [None]*size
        self.__rear = -1
        self.__front = -1

    def empty(self):
        return True    