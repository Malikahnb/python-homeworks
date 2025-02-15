# Ask the user for a sentence and create an acronym from the first letters of each word.
# Example:
#
# Input: "World Health Organization"
# Output: "WHO"

txt = input("Enter a sentence: ")
acronym = "".join(word[0].upper() for word in txt.split())
print(acronym)
