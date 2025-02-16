# Filter Even Numbers: Given a list of integers, create a new list that
# contains only the even numbers.

lst = [1, 2, 6, 3, 4, 5, 6, 7, 8, 2, 9, 10]
new_lst = []

for i in lst:
    if i % 2 == 0:
        new_lst.append(i)
    else:
        pass

print(new_lst)