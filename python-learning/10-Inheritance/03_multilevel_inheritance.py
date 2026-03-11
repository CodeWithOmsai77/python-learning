class employee:
    a = 1
class Programmer(employee):
    b = 2
class Manager(Programmer):
    c = 3
    
o = employee()
print(o.a) # prints the a attribute
# print(o.b) # Shows an error as ther is no b attribute in employee class 

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)