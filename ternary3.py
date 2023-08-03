def find_bigger_number(a: float, b: float, c: float) -> float:
    """
    Find the largest number among three values.
    
    This function takes three numeric values and determines the largest among them.
    
    Parameters:
    a (float): The first numeric value.
    b (float): The second numeric value.
    c (float): The third numeric value.
    
    Returns:
    float: The largest value among the three, or "Equal" if all three values are equal.
    """
    result = max(a, b, c) if a != b != c else "Equal"
    return result

# Testing the function
num1, num2, num3 = 10, 20, 30
result = find_bigger_number(num1, num2, num3)
print(f"Among {num1}, {num2}, and {num3}, the larger number is: {result}")
