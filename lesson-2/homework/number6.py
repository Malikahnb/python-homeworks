# Create a program that accepts a number and returns the last digit
# of that number.
number = int(input("Enter a number: "))
last_digit = number % 10

print("The last digit of", number, " is ", last_digit)