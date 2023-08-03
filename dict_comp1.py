# Create two lists: keys and values
keys = ["name", "age", "country", "language"]
values = ["Alice", 25, "USA", "English"]

# Create a dictionary using a dictionary comprehension and the zip function
result_dict = {key: value for key, value in zip(keys, values)}

# Print the resulting dictionary
print(result_dict)
