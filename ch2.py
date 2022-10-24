#print 2nd minimum number

n = int(input('size of list: '))
number = []
for i in range(n):
    num = int(input("Enter you number: "))
    number.append(num)

min = number[0]

for n in number:
    if n < min:
        min = n
    
number.pop(number.index(min))
min2 = number[0]
for n in number:
    if n < min2:
        min2 = n
 
print(min2)