'''Write a python function to remove a given word from a list and 
strip it at the same time.'''

def rem(l, word):
    n = [] # Create an empty list to store final result
    for item in l: # Loop through each element in the list/set
        if not(item == word): # Check if the element is NOT equal to given word
             # strip(word) removes characters of 'word' from start and end
            n.append(item.strip(word)) # Add cleaned word to new list
    return n  # Return the final list

l = {"Omsai", "Rohan", "an", "naman"}
print(rem(l, "sai"))