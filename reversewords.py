from http.cookiejar import FileCookieJar


class Stack:

    def __init__(self):
        self.item = []

    def size(self):
        return len(self.item)
        
    def isempty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self,item):
        self.item.append(item)


    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            return self.item.pop() 

    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            return self.item[-1]


str = input('>>> ')
s = Stack()
temp = ""
for i in str:
    if i == ' ':
        s.push(temp)
        temp=""
    else:
        temp+=i
s.push(temp)
for i in range(s.size()):
    print(s.pop(),end=" ")
