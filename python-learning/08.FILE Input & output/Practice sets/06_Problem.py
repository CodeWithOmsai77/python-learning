# Write a program to mine a log file and find out whether it contains ‘python’.

with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes python is present in the content")
else:
    print("No python is not present in content")