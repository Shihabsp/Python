# convert the temperature in degree centigrade to fahrenheit
#f=(9*c)/5+32
def convert(c):
    f = 9*c/5+32
    return f
    
temperature = float(input("Enter temperature in centigrade: "))
f = convert(temperature)
print(f'{f} degree fahrenheit')