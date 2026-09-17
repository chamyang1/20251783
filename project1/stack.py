class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item

    def pop(self):
        if not self.isEmpty():
            item = self.array[self.top]
            self.top -= 1
            return item

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
    
s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
print(f"peek : {s.peek()}")
print(f"pop : {s.pop()}")
print(f"peek : {s.peek()}")
print(f"isEmpty : {s.isEmpty()}")