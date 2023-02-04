print('Hello, Python!')

num1 = int(input('Plz input num1: '))
num2 = int(input('Plz input num2: '))

print(num1 + num2)

def subtract(): 
    a= int(input('input num1 for sub:'))
    b= int(input('input num2 for sub:'))
    c=a-b
    return c

c=subtract()
print('number returned is '+ str(c) )
