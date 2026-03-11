class employee:
    company = "Infosis"
    name = "default name"
    def show(self):
        print(f"the name is {self.name}and the salary is {self.company}")
    
class coder:
    language = "python"
    def printlanguage(self):
        print(f"out of all the languages her is your language: {self.language}")

class programmer(employee, coder):
    def showlanguage(self):
        print(f"The name is {self.company} and he is good in {self.language} language")
        
a = employee()
b = programmer()
b.show()
b.printlanguage()
b.showlanguage()