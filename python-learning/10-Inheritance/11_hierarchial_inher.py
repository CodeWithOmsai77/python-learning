class Employee:
    def attendance(self):
        print("Attendance marked")

class Developer(Employee):
    def develop(self):
        print("Develops software")

class Tester(Employee):
    def test(self):
        print("Tests software")

d = Developer()
t = Tester()

d.attendance()
d.develop()

t.attendance()
t.test()
