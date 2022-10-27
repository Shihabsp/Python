'''
implement queue
'''
from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()

    def size(self):
        return len(self.data)

    def isempty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            return self.data.popleft()

    def peek(self):
        if self.isempty():
            print("Queue is empty")
        else:
            return self.data[0]

q = Queue()
q.enqueue(1)
q.enqueue(4)
q.enqueue(2)
q.enqueue(3)
print(q.peek())
print(q.data)
q.dequeue()
print(q.peek())
print('After dequeue:', q.data)
print(q.data)

