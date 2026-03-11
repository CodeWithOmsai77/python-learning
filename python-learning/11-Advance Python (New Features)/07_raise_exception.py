a = int(input("enter your number: "))
b = int(input("enter second number: "))
# by doing this when we divide any number with zero then ZeroDivision error appear:- print(f"the division of a/b is {a/b}") 

# This is to add an error written in a differnt way for that we use the:- "Raise" function
if(b==0):
    raise ZeroDivisionError("Heyy, we cannot divide any number by zero")
else:
    print(f"the division of a/b is {a/b}")