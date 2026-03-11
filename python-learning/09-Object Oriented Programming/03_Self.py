class Employee:
    language = "Python" # This is a class artribute
    salary = "12000000"

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod       # this if we not need any object
    def greet():
        print("Good Morning")

omsai = Employee()
omsai.language = "java script" # This is object atribute

omsai.getinfo()
omsai.greet()
# Employee.getinfo(omsai)