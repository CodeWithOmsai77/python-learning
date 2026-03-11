# Write a program using functions to find greatest of three numbers.

a1 = int(input("enter your number: "))
b1 = int(input("enter your number: "))
c1 = int(input("enter your number: "))

def greatest(a1, b1, c1):
    if(a1>b1):
        return a1
    elif(b1>c1):
        return b1
    elif(c1>a1):
        return c1
    
'''a1 = int(input("enter your number: "))
b1 = int(input("enter your number: "))
c1 = int(input("enter your number: "))
'''
print(greatest(a1, b1, c1))