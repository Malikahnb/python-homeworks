# Write a program that checks if a string starts with one word and ends with another.
# Example:
#
# Input: "Python is fun!"
# Starts with: "Python"
# Ends with: "fun!"

txt = input("Enter a string: ")
start_w = input("Enter the starting word: ")
end_w = input("Enter the ending word: ")

if txt.startswith(start_w) and txt.endswith(end_w):
    print(f"The string starts with '{start_w}' and ends with '{end_w}'.")
else:
    print("The string does not start with '{start_w}' or does not end with '{end_w}'.")
