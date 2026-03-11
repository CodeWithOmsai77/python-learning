'''Write a program to create a dictionary of Hindi words with values as 
their English translation. Provide user with an option 
to look it up!'''

words = {
    "madad": "help",
    "naam": "name",
    "billi": "cat",
    "Bhagwan": "God"
}

meaning = input("Enter the word you want menaning: ")
print(words[meaning])