# 4. Write a program to filter a list of numbers which are divisible by 5.

def divisable5(n):
    if (n%5 == 0):
        return True 
    return False

a = [1, 22554, 55, 45, 788, 333, 45487, 7874, 255, 455525]

f = list(filter(divisable5, a))
print(f)