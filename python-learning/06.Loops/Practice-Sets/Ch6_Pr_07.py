'''Write a program to print the following star pattern.
  *
 ***
***** for n = 3'''

n = int(input("enter your number: "))

for i in range(1, n+1):
    # Print leading spaces to center the stars
    # (n - i) spaces are printed in each row
    print(" " * (n-i), end="")
     # Print stars in odd numbers: 1, 3, 5, ...
    # Formula (2 * i - 1) gives odd numbers
    print("*" * (2 * i-1), end="")
    print("")  # Move to the next line after printing one row