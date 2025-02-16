# Get Middle Element: Given a list, find the middle element. If the
# list has an even number of elements, return the two middle elements.

lst = [1, 2, 6, 3, 2, 9, 10, 11]
a = len(lst)
mid = a // 2

if a % 2 == 0:
    print(lst[mid -1], lst[mid])
else:
    print(lst[mid])