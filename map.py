def square_numbers(numbers):
    squared = map(lambda x: x ** 2, numbers)
    return list(squared)

# Testing the function
input_numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(input_numbers)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
