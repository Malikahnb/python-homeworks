# Find All Indices: Given a list and an element, find all the
# indices of that element in the list.

lst = [1, 6, 2, 6, 3, 4, 5, 6, 7, 8]
el = 6
indices = []

for i in range(len(lst)):
    if lst[i] == el:
        indices.append(i)

print(indices)