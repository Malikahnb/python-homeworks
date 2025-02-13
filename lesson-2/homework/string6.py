string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if string2 in string1:
    print(f"'{string2}' is found in '{string1}'")
else:
    print(f"'{string2}' is not found in '{string1}'")