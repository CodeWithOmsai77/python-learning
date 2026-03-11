'''Write a program to find out whether a given post is talking about
“Omsai” or not.'''

post = input("Enter you post: ")

if("Omsai".lower() in post.lower()):
# if ("Omsai" or "omsai" in post):
    print("You are taking about Omsai")

else:
    print("You are not talking about Omsai")