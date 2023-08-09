"""
This script defines a function to search a log file for lines containing a specific keyword.
"""

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
        with open(log_file, 'r', encoding='utf-8') as file:
            # Iterate through each line in the file
            for line in file:
                if search_keyword in line:
                    # If the search keyword is found in the line, print it
                    print(line.strip())
    except FileNotFoundError:
        # Handle the case where the specified file is not found
        print(f"Error: File '{log_file}' not found.")

if __name__ == "__main__":
    # Usage example
    LOG_FILE = "data/example.log"
    SEARCH_KEYWORD = "ERROR"

    # Call the function to search the log file for the specified keyword
    search_log(LOG_FILE, SEARCH_KEYWORD)
