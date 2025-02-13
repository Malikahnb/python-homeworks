# Create a program to ask name and year of birth from
# user and tell them their age.

name = input('Enter your name: ')
year = int(input('Enter your birth year: '))
age = 2025 - year

print(name, 'is', age, 'years old')