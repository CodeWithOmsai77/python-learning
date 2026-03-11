try:
    a = int(input("enter a number: "))
    print(a)

except Exception as e:
    print(e)

# Finally is run even if the program return as error 
finally:
    print("thank you")