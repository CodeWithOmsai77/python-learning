# Base class
class Employee:
    def login(self):
        print("Employee logged in")

# Derived class
class Developer(Employee):
    def code(self):
        print("Developer writes code")

dev = Developer()
dev.login()   # inherited
dev.code()    # own method
