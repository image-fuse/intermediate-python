from typing import Union

def sum_of_numbers(*args: Union[int, float]) -> Union[int, float]:
    """
    Calculate the sum of a variable number of input numbers.
    
    This function takes any number of numeric arguments and returns their sum.
    
    Parameters:
    *args (numeric): Any number of numeric arguments to be summed.
    
    Returns:
    Union[int, float]: The sum of the input numeric arguments.
    """
    return sum(args)

# Testing the function
print(sum_of_numbers(1, 2, 3))             # Output: 6
print(sum_of_numbers(10, 20, 30, 40))     # Output: 100
print(sum_of_numbers(2.5, 3.7, 1.2, 5.6)) # Output: 13.0
