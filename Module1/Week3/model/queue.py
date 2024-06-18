class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.__capacity

    def enqueue(self, val):
        if self.is_full():
            raise ValueError('Queue is full')
        self.items.append(val)

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self.items[0]
