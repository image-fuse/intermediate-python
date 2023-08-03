def check_odd_even(number):
    result = "Even" if number % 2 == 0 else "Odd"
    return result

# Testing the function
input_number = 7
result = check_odd_even(input_number)
print(f"The number {input_number} is {result}")  # Output: The number 7 is Odd
