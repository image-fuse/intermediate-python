from functools import reduce

def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    This function calculates the factorial of a non-negative integer using the reduce function.
    
    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.
    
    Returns:
    int: The factorial of the input integer.
    
    Raises:
    ValueError: If the input integer is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        # Use the reduce function and lambda expression to calculate the factorial
        return reduce(lambda x, y: x * y, range(2, n + 1))

# Testing the function
input_number = 5
factorial = calculate_factorial(input_number)
print(f"The factorial of {input_number} is {factorial}")  # Output: The factorial of 5 is 120
