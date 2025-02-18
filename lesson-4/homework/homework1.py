list1 = input("Enter the first list: ").split()
list2 = input("Enter the second list: ").split()


result = []

for i in list1:
    for j in list2:
        if i not in list2:
            if j not in list1:
                result.append(i)
                result.append(j)


print(result)