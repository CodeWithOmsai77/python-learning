class employee:
    lang = "python"
    salary = "100"
    name1 = "omsai"
    name2 = "paras"
    
    def getinfo(self):
        print(f"name is {self.name1}. language is {self.lang}. Salary is {self.salary}")
    
    def getinfo(self):
        print(f"name is {self.name2}. language is {self.lang}. salary is {self.salary}")
        
omsai = employee()
omsai.lang = "Js" # This give NEW ATTRIBUTE only for omsai
omsai.salary = "450" # This also shows that if we add a new attribute for a omsai it remains for him only doesnot change the info of other employee 
omsai.getinfo()

paras = employee()
paras.getinfo()
