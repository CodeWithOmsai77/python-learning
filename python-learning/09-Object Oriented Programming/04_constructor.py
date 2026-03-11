class Employee:
    language = "Python" # This is a class artribute
    salary = "12000000"
    
    def __init__(self, name, salary, language):             # is is use to call the dunder method using the __init__ option
        self.name = name
        self.salary = salary
        self.language = language
        print("i am learning objects")    # this above is constructor method to print an object in python programming
        
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod       # this if we not need any object
    def greet():
        print("Good Morning")

omsai = Employee("Omsai", 150000, "javascript")
omsai.name = "Omsai" # This is object atribute
print(omsai.name, omsai.salary, omsai.language)
omsai.greet()