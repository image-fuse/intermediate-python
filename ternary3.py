def find_bigger_number(a, b, c):
    result = max(a, b, c) if a != b != c else "Equal"
    return result

# Testing the function
num1, num2, num3 = 10, 20, 30
result = find_bigger_number(num1, num2, num3)
print(f"Among {num1}, {num2}, and {num3}, the larger number is: {result}")
