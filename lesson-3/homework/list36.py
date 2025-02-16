# Sum of Positive Numbers: Given a list of numbers, calculate the sum of all positive numbers.

lst = [-5, -3, -1, 0, 2, 4, 6, -2, 8, -4]
counter = 0

for i in range(len(lst)):
    if lst[i] > 0:
        counter += lst[i]
    else:
        pass


print(counter)
        