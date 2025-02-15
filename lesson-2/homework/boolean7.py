# Write a program that checks if the sum of two numbers is greater than 50.8. Create a program that checks if a given number is between 10 and 20 (inclusive)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if (num1 + num2) > 50.8:
    print("The sum is greater than 50.8.")
else:
    print("The sum is not greater than 50.8.")


num = float(input("Enter a number: "))

if 10 <= num <= 20:
    print("The number is between 10 and 20 (inclusive).")
else:
    print("The number is not in the range.")
