class Company:
    def company_name(self):
        print("ABC Tech")

class Manager(Company):
    def manage(self):
        print("Manages team")

class TeamLead(Manager):
    def lead(self):
        print("Leads developers")

t = TeamLead()
t.company_name()
t.manage()
t.lead()
