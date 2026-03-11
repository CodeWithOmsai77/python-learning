# try:
#     a = int(input("enter a number: "))
#     print(a)

# except Exception as e:
#     print(e)
# else: 
#     print("i am in else")

try:
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    print(f"Divission is {a / b}")
except ZeroDivisionError:
    print("Division is not possible")
else:
    print("Division is successfull")