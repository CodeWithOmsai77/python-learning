class employee:
        def __init__(self):
            print("Constrctr of Employee")
        a = 1
class Programmer(employee):
        def __init__(self):
            print("Constrctr of Programmer")
        b = 2
class Manager(Programmer):
        def __init__(self):
            super().__init__()
            print("Constrctr of Manager")
        c = 3
    
# o = employee()
# print(o.a) # prints the a attribute
# print(o.b) # Shows an error as ther is no b attribute in employee class 

# o = Programmer()
# # print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)