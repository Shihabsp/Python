# print a number even or odd
def check(num):
    if(num%2==0):
        return True
    else:
        return False

number = int(input("Enter a number: "))
if(number!=0):
    result = check(number)
    if(result == True):
        print(f'{number} is even')
    elif(result == False):
        print(f'{number} is odd')
else:
    print(f'{number} is even or odd')