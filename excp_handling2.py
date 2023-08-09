"""
This script reads the contents of a file specified by the user and prints them.
"""

def main():
    """
    Main function to read and display file contents.
    """
    try:
        # Prompt the user to input a filename
        filename = input("Enter the filename: ").strip()

        # Try to open the file for reading using a 'with' statement
        with open(filename, 'r', encoding='utf-8') as file:
            # Read the contents of the file
            contents = file.read()

            # Print the file contents
            print("File Contents:")
            print(contents)

    except FileNotFoundError:
        # Handle the case where the specified file is not found
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    main()
