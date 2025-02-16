# Create Nested List: Create a new list that contains sublists, where
# each sublist contains a specified number of elements from the original list.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist_size = 3

nested_list = [lst[i:i + sublist_size] for i in range(0, len(lst), sublist_size)]

print(nested_list)
