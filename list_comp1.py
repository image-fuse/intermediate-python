# Original list of strings
original_list = ["apple", "banana", "grape", "orange", "strawberry", "kiwi", "pear"]

# Create a filtered list containing strings with length greater than 5
filtered_list = [string for string in original_list if len(string) > 5]

# Print the filtered list
print(filtered_list)
