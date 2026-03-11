"""Write a python program to print the contents of a directory using the os module.
 Search online for the function which does that.
 &
 Label the program written in problem 4 with comments"""

import os

# to difine the path
path = "/Study Material"

# to execute the path
files = os.listdir(path)

# To print the items which is executed 
for item in files:
    print(item)
