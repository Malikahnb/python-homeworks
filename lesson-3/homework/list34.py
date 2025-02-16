# Rotate List: Given a list, create a new list that is a rotated
# version of the original list (shift elements to the right).

lst = [1, 2, 3, 4, 5]
shift = 2

shift = shift % len(lst)
rotated_list = lst[-shift:] + lst[:-shift]

print(rotated_list)
