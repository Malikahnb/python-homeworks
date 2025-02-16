# Get Unique Elements in Order: Given a list, create a new list that
# contains unique elements while maintaining the original order.

lst = [1, 2, 3, 2, 4, 1, 5, 3, 6]

unique= []
for i in lst:
    if i not in unique:
        unique.append(i)

print(unique)
