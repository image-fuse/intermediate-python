import json

def add_to_json(filename, new_data):
    try:
        with open(filename, 'r') as file:
            existing_data = json.load(file)
        
        existing_data.append(new_data)
        
        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4)
            
        print("Data has been added to the JSON file.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Sample JSON data
filename = "data/data.json"
new_data = {
    "name": "Laxman",
    "age": 28
}

add_to_json(filename, new_data)
