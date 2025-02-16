# Remove Element by Index: Given a list and an index, remove the
# element at that index if it exists.

lst = [1, 5, 3, 9, 2, 8, 4, 7]
ind = 7

if len(lst) - 1 >= ind:
    lst.pop(ind)
    print(lst)
else:
    print("Not found")