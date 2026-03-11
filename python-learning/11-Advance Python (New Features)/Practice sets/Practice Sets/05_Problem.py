# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
a = [1, 22554, 55, 45, 788, 333, 45487, 7874, 255, 455525]

def greater(a, b):
    if (a>b):
        return a
    return b

print(reduce(greater, a))