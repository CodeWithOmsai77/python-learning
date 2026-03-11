a = int(input("Enter your age: "))

# If statement number 1
if(a%2 == 0):
    print("a is even")
# End of if statement 1

# If statement number 2
if(a>=18):
    print("Your age is above concent")

elif(a<0):
    print("Age cannot be negative")

elif(a==0):
    print("0 is not a valid age")

else:
    print("you are below age of concent")
# End of if statement 2

print("\n\tEnd of the program")