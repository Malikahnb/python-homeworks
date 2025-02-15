# Ask the user for a string and replace all the vowels with a symbol (e.g., *).

txt = input("Enter a string: ")
vowels = "AEIOUaeiou"

# Replace vowels with '*'
no_vowels = "".join("*" if char in vowels else char for char in txt)

print(no_vowels)
