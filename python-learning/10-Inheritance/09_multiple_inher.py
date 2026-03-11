class Backend:
    def backend_skill(self):
        print("Works with databases")

class Frontend:
    def frontend_skill(self):
        print("Works with UI")

class FullStack(Backend, Frontend):
    def role(self):
        print("Full Stack Developer")

fs = FullStack()
fs.backend_skill()
fs.frontend_skill()
fs.role()
