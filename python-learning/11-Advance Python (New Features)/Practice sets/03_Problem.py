# 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

n = int(input("Enter the number: "))
table = [str(n*i) for i in range (1, 11)]

s = "\n".join(table)
print(s)