'''Write a program to greet all the person names stored in a list 'l' 
and which starts with S.'''


l = ["Omsai", "Soham", "Sachin", "Rahul", "Sahil", "sanika"]

for name in l:
    if "s" in name.lower():
        print(f"Hello {name}")
        


