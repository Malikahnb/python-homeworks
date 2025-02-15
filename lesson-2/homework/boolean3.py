# Write a program that checks if a number is positive and even.

num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is NOT positive and even.")