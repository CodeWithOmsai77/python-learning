# 3. Create a class ‘Employee’ and add salary and increment properties to it. Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.

class employee:
    salary = 256
    increment = 40
    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary * (self.increment/100)) 
    @salaryafterincrement.setter
    def salaryafterrincrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100
e = employee()
# print(e.salaryafterincrement)
e.salaryafterrincrement = 280
print(e.increment)