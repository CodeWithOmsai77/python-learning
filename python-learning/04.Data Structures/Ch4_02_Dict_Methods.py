d = {} # This define empty dict

marks = {
    "omsai": 100,
    "shubham": 78,
    "Om": 99,
    0:"sahil"
}

# print(marks.items())  #It shows all items of dictonary
# print(marks.keys())   #it shows only keys means "Omsai" of dictnary
# print(marks.values())   #it shows only values means the marks of items

# marks.update({"omsai": 99, "Aryan": 85}) # It udpadte means add any new value or item as per required
# print(marks.get("omsai2")) # returns NONE
# print(marks["Omsai2"]) # Returns an error
marks.pop("omsai") # Remove or pop an item
print(marks)