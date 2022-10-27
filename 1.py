'''
print 7 days average temperature
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
sum = 0
for i in range(7):
    tem = float(input("Today's temperature: "))
    q.enqueue(tem)
    sum += tem
    avg = sum/(i+1)
    print(f'7-day average temperature: {avg}')
