try:
    # Prompt the user to input an integer
    user_input = input("Enter an integer: ")
    
    # Convert the user input to an integer
    number = int(user_input)
    
    # Print the successfully converted integer
    print(f"Successfully converted to integer: {number}")
    
except ValueError:
    # Handle the case where the input cannot be converted to an integer
    print("Error: Input cannot be converted to an integer.")
