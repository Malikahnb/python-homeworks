# Create a program that accepts two strings and checks if they have the same length.

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) == len(string2):
    print("Both strings have the same length.")
else:
    print("The strings have different lengths.")
