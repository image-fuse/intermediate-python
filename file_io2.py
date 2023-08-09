"""
This script defines a function to add new data to an existing JSON file.
"""

import json
from typing import Dict, Any

def add_to_json(filename: str, new_data: Dict[str, Any]) -> None:
    """
    Add new data to an existing JSON file.

    This function reads the existing JSON data from the specified file,
    appends the new data to it, and then writes the updated data back to the file.

    Parameters:
    filename (str): The name of the JSON file to which data will be added.
    new_data (dict): The new data to be added, represented as a dictionary.

    Returns:
    None
    """
    try:
        # Read the existing JSON data from the file
        with open(filename, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)

        # Append the new data to the existing data
        existing_data.append(new_data)

        # Write the updated data back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, indent=4)

        print("Data has been added to the JSON file.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    # Sample JSON data
    FILENAME = "data/data.json"
    NEW_DATA = {
        "name": "Laxman",
        "age": 28
    }

    # Call the function to add new data to the JSON file
    add_to_json(FILENAME, NEW_DATA)
