# Input list of numbers
numbers = [2, 5, 8, 10, 15, 12, 7, 4, 10]

# Create a set containing even numbers from the list
even_numbers_set = {num for num in numbers if num % 2 == 0}

# Print the resulting set of even numbers
print(even_numbers_set)
