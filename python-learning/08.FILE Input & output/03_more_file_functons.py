f = open("file.txt")

# this is used to print all line in a single line as a list
lines = f.readlines()
print(lines, type (lines))  

# This is used to print all lines separate in numbering form
# line1 = f.readline()
# print(line1, type (line1))

# line2 = f.readline()
# print(line2, type (line2))

# line4 = f.readline()
# print(line4, type (line4))

# line4 = f.readline()
# print(line4, type (line4))

# line5 = f.readline()
# print(line5, type (line5))

# line6 =  f.readline()
# print(line6 == "")

# In this we use a while loop to print all the lines 
# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()

f.close()