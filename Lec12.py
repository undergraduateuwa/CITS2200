
class Q:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        """入队"""
        if self.is_full():
            raise OverflowError("enqueue on full queue")
        self.data[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        """出队并返回元素"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        """查看队首元素但不移除"""
        if self.is_empty():
            return None
        return self.data[self.head]



q = Q()



