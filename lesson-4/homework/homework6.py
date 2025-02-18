# Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.

for i in range(1, 101):
    if i % 1 == 0 and i % i == 0:
        print(i)