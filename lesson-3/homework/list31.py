# Repeat Elements: Given a list and a number, create a new list where
# each element is repeated that number of times.

lst = [1, 5, 3, 9, 2, 8, 4, 7]
num = 2
new = []

for i in lst:
    for j in range(num):
        new.append(i)

print(new)