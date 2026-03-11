'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3 or any modified 
*
'''
p = int(input("Enter your number: "))
def pattern(p):
    for i in range(p, 0, -1): # Loop starts from p and decreases 
# i by 1 each time until it reaches 1 (-1 used for reverse pattern)
        print ("*" * i)
    return ""

print(pattern(p) , end="")