def check_odd_even(number: int) -> str:
    """
    Check if a number is odd or even.
    
    This function takes an integer as input and checks if it's odd or even.
    
    Parameters:
    number (int): The integer to be checked.
    
    Returns:
    str: A string indicating whether the number is "Even" or "Odd".
    """
    result = "Even" if number % 2 == 0 else "Odd"
    return result

# Testing the function
input_number = 7
result = check_odd_even(input_number)
print(f"The number {input_number} is {result}")  # Output: The number 7 is Odd
