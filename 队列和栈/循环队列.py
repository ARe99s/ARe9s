class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * (k + 1)
        self.head = 0
        self.tail = 0
        self.size = len(self.queue)
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count += 1
        print(f'count{self.count}')
        print(f'tail{self.tail}')
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        res = self.queue[self.head]
        return res

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        res = self.queue[((self.tail - 1) % self.size)]
        return res

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return (self.tail + 1) % self.size == self.head
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()