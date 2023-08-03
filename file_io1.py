import csv

# Read data from "data.csv" and write filtered data to "adults.csv"
with open('data/data.csv', 'r', newline='') as input_file, open('data/adults.csv', 'w', newline='') as output_file:
    # Create a CSV reader object for the input file
    reader = csv.DictReader(input_file)
    
    # Get the field names from the input file
    fieldnames = reader.fieldnames
    
    # Create a CSV writer object for the output file
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    
    # Write the header (field names) to the output file
    writer.writeheader()
    
    # Iterate through each row in the input file
    for row in reader:
        age = int(row['Age'])  # Convert the 'Age' value to an integer
        if age >= 18:  # Check if the age is 18 or older
            writer.writerow(row)  # Write the row to the output file

# Print a message indicating that the filtering process is complete
print("Filtered data has been written to 'data/adults.csv'.")
