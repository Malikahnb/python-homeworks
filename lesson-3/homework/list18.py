# Find Sublist: Given a list and a sublist, check if the sublist
# exists within the list.

lst = [1, 2, 6, 3, 4, 5, 6, 7, 8, 2, 9, 10]
sublst = [2, 6, 3]

n, m = len(lst), len(sublst)
for i in range(n - m + 1):
    if lst[i:i + m] == sublst:
        print(True)
    else:
        print(False)