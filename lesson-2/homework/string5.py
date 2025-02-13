text = input("Enter a string: ")

# Initialize vowel and consonant counters
vowels = 0
consonants = 0

# Define vowels
vowel_set = "aeiouAEIOU"

# Count vowels and consonants
for char in text:
    if char.isalpha():
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1

# Print the results
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")