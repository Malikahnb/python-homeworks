# Write a program that takes three numbers and checks if all of
# them are different.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 != num2 and num1 != num3 and num2 != num3:
    print("All numbers are different.")
else:
    print("Some numbers are the same.")
