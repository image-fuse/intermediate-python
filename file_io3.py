def search_log(log_file: str, search_keyword: str) -> None:
    """
    Search a log file for lines containing a specific keyword.
    
    This function reads the specified log file, line by line, and prints
    any lines that contain the given search keyword.
    
    Parameters:
    log_file (str): The path to the log file to be searched.
    search_keyword (str): The keyword to search for in the log file.
    
    Returns:
    None
    """
    try:
        # Open and read the log file
        with open(log_file, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                if search_keyword in line:
                    # If the search keyword is found in the line, print it
                    print(line.strip())
    except FileNotFoundError:
        # Handle the case where the specified file is not found
        print(f"Error: File '{log_file}' not found.")

# Usage example
log_file = "data/example.log"
search_keyword = "ERROR"

# Call the function to search the log file for the specified keyword
search_log(log_file, search_keyword)
