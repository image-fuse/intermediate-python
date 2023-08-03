class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age should be between 0 and 120.")

def get_valid_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0 or age > 120:
                raise InvalidAgeError(age)
            return age
        except ValueError:
            print("Invalid input. Please enter a valid age as a number.")
        except InvalidAgeError as e:
            print(e)

def main():
    age = get_valid_age()
    print(f"Your age is: {age}")

if __name__ == "__main__":
    main()