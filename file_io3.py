def search_log(log_file, search_keyword):
    try:
        with open(log_file, 'r') as file:
            for line in file:
                if search_keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")

# Usage example
log_file = "data/example.log"
search_keyword = "ERROR"

search_log(log_file, search_keyword)
