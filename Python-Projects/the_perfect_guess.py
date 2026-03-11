import random
n = random.randint(1, 100)
a = -1
guesses = 0
while (a != n):
    a = int(input("guess a number: "))
    if (a>n):
        print("lower number please")
        guesses +=1
    elif(a<n):
        print("higher number please")
        guesses +=1 
    
print(f"You have guess the number {n} in {guesses} attepts")