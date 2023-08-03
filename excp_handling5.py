# Define a custom exception class for handling invalid age values
class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age should be between 0 and 120.")

# Function to input and validate age within a specified range
def get_valid_age():
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
        except InvalidAgeError as e:
            print(e)  # Print the error message from the custom exception

# Main function to demonstrate age validation
def main():
    age = get_valid_age()  # Call the get_valid_age function
    print(f"Your age is: {age}")  # Print the validated age

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
