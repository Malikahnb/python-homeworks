# Count Even Numbers: Given a list of integers, count how many
# of them are even.

lst = [1, 2, 6, 3, 4, 5, 6, 7, 8, 2, 9, 10]
counter = 0

for i in lst:
    if i % 2 == 0:
        counter += 1
    else:
        pass

print(counter)