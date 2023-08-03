try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    
    result = num1 / num2
    
    print(f"The result of {num1} / {num2} is: {result}")
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")
