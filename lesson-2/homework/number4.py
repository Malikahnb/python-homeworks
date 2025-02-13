# Write a program that takes two numbers and prints out the result of
# integer division and the remainder.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

quotient = num1 // num2
remainder = num1 % num2

print("Quotient is: ", quotient)
print("Remainder is: ", remainder)