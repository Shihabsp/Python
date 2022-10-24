# find out the average of a set of integers
def average(num):
    sum = 0
    for i in range(len(num)):
        sum+=num[i]
    avr = sum/len(num)
    print (avr)

number = int(input("Enter the count of numbers: "))
list = []
for i in range(number):
    list.append(int(input("Enter a number: ")))
average(list)
