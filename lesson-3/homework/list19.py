# Replace Element: Given a list, replace the first occurrence
# of a specified element with another element.

lst = [1, 2, 3, 4, 2, 5]
old_value = 2
new_value = 99

if old_value in lst:
    index = lst.index(old_value)  # Find the first occurrence
    lst[index] = new_value  # Replace it

print(lst)