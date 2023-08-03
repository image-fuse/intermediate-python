from functools import reduce

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(2, n + 1))

# Testing the function
input_number = 5
factorial = calculate_factorial(input_number)
print(f"The factorial of {input_number} is {factorial}")  # Output: The factorial of 5 is 120
