# Write a program to check if a string contains any digits.

txt = input("Enter a string: ")

if any(i.isdigit() for i in txt):
    print("The string contains digits.")
else:
    print("The string does NOT contain any digits.")
