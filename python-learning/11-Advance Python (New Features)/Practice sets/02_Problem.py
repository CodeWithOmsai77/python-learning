# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

l = [1, 2, 5, 4, 5, 6, 7, 8, 9, 10]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)
