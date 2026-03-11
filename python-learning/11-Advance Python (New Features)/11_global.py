# ‘global’ keyword is used to modify the variable outside of the current scope.

a = 89

def fun():
    global a  # this prints the a globally means it will print a as many times we want that global keyword a 
    # a = 1
    print(a)
    
fun()
print(a)

print(a)