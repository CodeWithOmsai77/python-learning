# Write a program to find whether a given number is prime or not.

n = int(input("Enter Your Number: "))

for i in range(2, n): # Loop starts from 2 up to (n-1) to check divisibility
    if(n%i) == 0:     # Checks if n is divisible by i (remainder is 0)
        print("Your number is not prime")
        break
    else:
        print("Your number is prime")


