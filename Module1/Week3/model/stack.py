class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def is_empty(self):
        if self.items:
            return False
        return True

    def is_full(self):
        return len(self.items) >= self.__capacity

    def pop(self):
        if self.is_empty():
            return ValueError('Stack is empty')
        return self.items.pop(-1)

    def push(self, val):
        if self.is_full():
            raise ValueError('Stack is full')
        self.items.append(val)

    def top(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.items[-1]
