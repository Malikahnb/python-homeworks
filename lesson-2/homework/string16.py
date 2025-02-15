# Write a program that asks the user for a string and a
# character, then removes all occurrences of that character from the string.

txt = input("Enter a string: ")
ch = input("Enter the character to remove: ")

removed = txt.replace(ch, "")

print(removed)
