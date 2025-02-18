def uncommon_elements(list1, list2):
    result = []

    for num in list1:
        if num not in list2:
            result.append(num)

    for num in list2:
        if num not in list1:
            result.append(num)

    return result


# Test cases
print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # Output: [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # Output: [2, 2, 5]
