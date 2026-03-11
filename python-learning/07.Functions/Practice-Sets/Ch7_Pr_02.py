'''Write a python program using function to convert Celsius to 
Fahrenheit.'''

# c = 5*(f-32)/9 :- imp formula

f = int(input("Enter temperature: "))

def f_c(f):
    return 5*(f-32)/9
print("Conversion is: ")
c = f_c(f)
print(f"{round(c, 2)} °c")
