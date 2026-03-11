'''Write a program which finds out whether a given name is present in a list 
or not.'''

l = ["Omsai", "Om", "aditya", "parth", "paras"]

name = input("Enter your name: ")

if(name in l):
    print("Yes, Your name is in the list")

else:
    print("Your name is not in the list")