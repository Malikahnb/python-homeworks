# Last Element: Access the last element of a list, considering what
# to return if the list is empty.

lst = [1, 2, 6, 3, 4, 5, 6, 7, 8, 2, 9, 10]

if lst is None or len(lst) == 0:
    print("Empty list")
else:
    print(lst[-1])