'''
Write a python function which converts inches to cms.
*Centimeters = Inches X 2.54*
'''

inch = int(input("enter number in Inches: "))
def cms(inch):
    return inch * 2.54
print(cms(inch))