# Write a program that asks the user for a sentence and prints
# the number of words in it.

txt = input("Enter sentence: ")

num = txt.split()

print(len(num))