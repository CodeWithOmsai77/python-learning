'''It is used to reduce the complexity of the program. As we can see below that
for making average of three numbers we use "Def" function to use same avg functon 
multiple times insteed of typing same program again and again.'''


# Function defination:-
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c)/3
    print(average)

# Function call:- 
avg() # This is called function call.
print("thank you") # To print thank any where
avg() # This is called function call.
print("thank you")
avg() # This is called function call.
avg() # This is called function call.