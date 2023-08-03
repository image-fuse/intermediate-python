try:
    filename = input("Enter the filename: ")
    
    with open(filename, 'r') as file:
        contents = file.read()
        print("File Contents:")
        print(contents)
        
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
