try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
    
    print(f"Successfully converted to integer: {number}")
    
except ValueError:
    print("Error: Input cannot be converted to an integer.")
