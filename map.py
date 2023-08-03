def square_numbers(numbers: list) -> list:
    """
    Square each number in a list using the map function.
    
    This function takes a list of numbers and uses the map function along
    with a lambda expression to square each number in the list.
    
    Parameters:
    numbers (list): A list of numbers to be squared.
    
    Returns:
    list: A list containing the squared numbers.
    """
    # Use the map function and lambda expression to square each number
    squared = map(lambda x: x ** 2, numbers)
    
    # Convert the map object to a list and return the squared numbers
    return list(squared)

# Testing the function
input_numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(input_numbers)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
