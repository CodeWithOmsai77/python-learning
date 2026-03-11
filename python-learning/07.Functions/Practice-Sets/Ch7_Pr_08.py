# Write a python function to print multiplication table of a given number.

n = int(input("Enter your number: "))
def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

# n = 5
print(multiply(n))