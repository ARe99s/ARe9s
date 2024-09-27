class ArrayStack:
    def __init__(self, stackSize: int):
        self.stack = [0] * stackSize
        self.stackSize = stackSize
        self.top = 0

    def push(self, value: int) -> bool:
        if self.top >= self.stackSize:
            return False
        self.stack[self.top] = value
        self.top += 1
        return True

    def pop(self) -> int:
        if self.top == 0:
            return -1
        self.top -= 1
        return self.stack[self.top]

    def peek(self) -> int:
        if self.top == 0:
            return -1
        return self.stack[self.top - 1]

    def isEmpty(self) -> bool:
        if self.top == 0:
            return True
        else:
            return False
