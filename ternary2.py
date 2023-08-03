def check_leap_year(year):
    result = "Leap Year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a Leap Year"
    return result

# Testing the function
input_year = 2024
result = check_leap_year(input_year)
print(f"The year {input_year} is {result}")  # Output: The year 2024 is Leap Year
