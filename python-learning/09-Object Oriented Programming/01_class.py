class Employee:
    language = "Python" # This is a class artribute
    salary = "12000000"

# omsai is an object
Omsai = Employee()
Omsai.name = "Omsai" # This is object atribute
print(Omsai.name,Omsai.language, Omsai.salary)  # this is the class of that object

# Ram = Employee()
# Ram.name = "Ram"
# print(Ram.name, Ram.language, Ram.salary)

'''1. An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object instantiation.

2. Objects of a given class can invoke the methods available to it without revealing the implementation details to the user. - Abstractions & Encapsulation!'''