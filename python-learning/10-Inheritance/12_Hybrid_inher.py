class Company:
    def name(self):
        print("TechCorp")

class HR(Company):
    def hr_work(self):
        print("Handles recruitment")

class IT(Company):
    def it_work(self):
        print("Handles infrastructure")

class Admin(HR, IT):
    def admin_work(self):
        print("Manages company")

a = Admin()
a.name()
a.hr_work()
a.it_work()
a.admin_work()
