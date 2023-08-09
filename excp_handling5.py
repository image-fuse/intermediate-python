"""
This script defines a custom exception class for handling invalid age values,
implements a function to input and validate age within a specified range,
and demonstrates age validation through a main function.
"""

class InvalidAgeError(Exception):
    """
    Custom exception class for handling invalid age values.
    """
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age should be between 0 and 120.")

def get_valid_age():
    """
    Function to input and validate age within a specified range.
    """
    while True:
        try:
            # Ask the user to input their age
            age = int(input("Please enter your age: "))

            # Check if the age is outside the valid range (0 to 120)
            if age < 0 or age > 120:
                raise InvalidAgeError(age)  # Raise the custom exception

            return age  # If age is valid, return it

        except ValueError:
            print("Invalid input. Please enter a valid age as a number.")
        except InvalidAgeError as err:
            print(err)  # Print the error message from the custom exception

def main():
    """
    Main function to demonstrate age validation.
    """
    age = get_valid_age()  # Call the get_valid_age function
    print(f"Your age is: {age}")  # Print the validated age

if __name__ == "__main__":
    main()  # Call the main function to start the program
