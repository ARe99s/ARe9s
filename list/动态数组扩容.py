class MyArray:
    def __init__(self):
        self.capacity = 4
        self.data = [0] * self.capacity
        self.n = 0

    def insert(self, index: int, value: int)->bool:
        if index > self.n or index < 0:
            return False
        if self.capacity == self.n:
            new_data = [0] * (self.capacity * 2)
            for i in range(self.n):
                new_data[i] = self.data[i]
            self.capacity *= 2
            self.data = new_data
        for i in range(self.n-1, index-1, -1):  # 因为是倒着从后往前走，所以取到index-1
            self.data[i+1] = self.data[i]
        self.data[index] = value
        self.n += 1
        return True

    def delete(self, index: int)->int:
        if index < 0 or index >= self.n:
            return -1
        value = self.data[index]
        for i in range(index+1, self.n):  # 把删除元素后面的元素依次赋给前面
            self.data[i-1] = self.data[i]
        self.n -= 1
        return value

    def get(self, index: int)->int:
        if index < 0 or index >= self.n:
            return -1
        return self.data[index]