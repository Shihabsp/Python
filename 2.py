"""
implement queue using stack
"""

class Stack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def size(self):
        return len(self.s1)
        
    def isempty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self,data):
        self.s1.append(data)
        
    def pop(self):
        if self.isempty():
            print("Queue is empty")
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            temp = self.s2.pop()

            while self.s2:
                self.s1.append(self.s2.pop())
            return temp
        

    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            return self.s1[0]


s = Stack()
s.push(1)
s.push(4)
s.push(2)
s.push(3)
print(f'size of stack = {s.size()}')
print(s.s1)
print(f'peek of stack = {s.peek()}')

s.pop()
print(s.s1)
print(f'peek of stack = {s.peek()}')
s.pop()
print(s.s1)
print(f'size of stack = {s.size()}')
print(f'stack is empty = {s.isempty()}')
print(f'peek of stack = {s.peek()}')
s.pop()
print(f'stack is empty = {s.isempty()}')
print(f'size of stack = {s.size()}')
s.pop()
print(s.s1)