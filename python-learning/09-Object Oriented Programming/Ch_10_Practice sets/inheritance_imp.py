# Parent class (common for all employees)
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)

# Child class (special type of employee)
class Developer(Employee):
    def __init__(self, name, emp_id, language):
        # Call parent constructor
        super().__init__(name, emp_id)
        self.language = language

    def show_skill(self):
        print("Programming Language:", self.language)

# Creating object of child class
dev = Developer("Omsai", 101, "Python")

# Using inherited method
dev.show_details()

# Using child class method
dev.show_skill()
