try:
    # Prompt the user to input a filename
    filename = input("Enter the filename: ")
    
    # Try to open the file for reading using a 'with' statement
    with open(filename, 'r') as file:
        # Read the contents of the file
        contents = file.read()
        
        # Print the file contents
        print("File Contents:")
        print(contents)
        
except FileNotFoundError:
    # Handle the case where the specified file is not found
    print(f"Error: File '{filename}' not found.")
