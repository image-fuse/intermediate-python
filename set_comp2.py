# Input list of words
words = ["apple", "banana", "cherry", "date"]

# Create a set containing unique characters from the words
unique_characters_set = {char for word in words for char in word}

# Print the resulting set of unique characters
print(unique_characters_set)
