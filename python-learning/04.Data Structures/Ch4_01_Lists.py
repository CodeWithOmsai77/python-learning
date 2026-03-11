# Lists are used to Mutable (Changable) the elements

# Below are Lists
friends = ["Apple", "akash", "boy", "7", "smile00", "345.22", "Dasari"]

print(friends[3])
friends[0] = "Omsai" # Unlike Strings Lists are mutable (Changable)

friends.append("Omsai")
print(friends)

# Below are Methods of lists
L1 = [1, 32, 5, 252,553, 0, 88, 9]
L1.sort() # it is used sort the list in accending order
L1.reverse() # It is used to reverse the List 
L1.insert(3, 6767) # Insert any element at position 3
print(L1.pop(3)) # print the specific element only
value = L1.pop(3) # pop the required element 
print(value)
print(L1.remove(553))

print(L1)
