def check_leap_year(year: int) -> str:
    """
    Check if a year is a leap year.
    
    This function takes a year as input and checks if it's a leap year or not.
    
    Parameters:
    year (int): The year to be checked.
    
    Returns:
    str: A string indicating whether the year is a "Leap Year" or "Not a Leap Year".
    """
    result = "Leap Year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a Leap Year"
    return result

# Testing the function
input_year = 2024
result = check_leap_year(input_year)
print(f"The year {input_year} is {result}")  # Output: The year 2024 is Leap Year
