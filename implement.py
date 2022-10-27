""""
implement stack 
"""
class Stack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)
        
    def isempty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self,data):
        self.data.append(data)


    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            return self.data.pop() 

    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            return self.data[-1]

    

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(f'size of stack = {s.size()}')
print(s.data)
print(f'peek of stack = {s.peek()}')

s.pop()
print(f'peek of stack = {s.peek()}')
s.pop()
print(f'size of stack = {s.size()}')
print(f'stack is empty = {s.isempty()}')
print(f'peek of stack = {s.peek()}')
s.pop()
print(f'stack is empty = {s.isempty()}')
print(f'size of stack = {s.size()}')
s.pop()
print(s.data)


