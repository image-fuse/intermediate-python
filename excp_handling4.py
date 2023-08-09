"""
This script prompts the user to input the numerator and denominator, performs division, 
and displays the result.
"""

def main():
    """
    Main function to prompt for numerator and denominator, perform division, and display the result.
    """
    try:
        # Prompt the user to input the numerator and denominator
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))

        # Perform the division and calculate the result
        result = num1 / num2

        # Print the result of the division
        print(f"The result of {num1} / {num2} is: {result:.2f}")

    except ZeroDivisionError:
        # Handle the case where the denominator is zero
        print("Error: Division by zero is not allowed.")
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Error: Please enter valid integers.")

if __name__ == "__main__":
    main()
