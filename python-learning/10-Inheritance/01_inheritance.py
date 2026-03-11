class employee:
    company = "Infosis"
    def show(self):
        print(f"the name is {self.name}and the salary is {self.salary}")
    
# class programmer:
#     company = "Infosis ltd"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
#     def showlanguage(self):
#         print(f"the name is {self.name} and he is good with {self.languge} language")

class programmer(employee):
    def showlanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")
        
a = employee()
b = programmer()
print(a.company, b.company)