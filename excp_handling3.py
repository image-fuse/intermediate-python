"""
This script prompts the user to input an integer, converts it, and displays the result.
"""

def main():
    """
    Main function to prompt for an integer, convert, and display the result.
    """
    try:
        # Prompt the user to input an integer
        user_input = input("Enter an integer: ").strip()

        # Convert the user input to an integer
        number = int(user_input)

        # Print the successfully converted integer
        print(f"Successfully converted to integer: {number}")

    except ValueError:
        # Handle the case where the input cannot be converted to an integer
        print("Error: Input cannot be converted to an integer.")

if __name__ == "__main__":
    main()
