# Write a program to read the text from a given file 'poems.txt' 
# and find out whether it contains the word 'twinkle'.

poem = open("poem.txt")
content = poem.read()
if("Twinkle".lower() in content.lower()):
    print("Twinkle is present in the content\n")
else:
    print("Twinkle is not present in the content\n")
# print (content)
poem.close()

