import csv

# Read data from "data.csv" and write filtered data to "adults.csv"
with open('data/data.csv', 'r', newline='') as input_file, open('data/adults.csv', 'w', newline='') as output_file:
    reader = csv.DictReader(input_file)
    fieldnames = reader.fieldnames
    
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        age = int(row['Age'])
        if age >= 18:
            writer.writerow(row)

print("Filtered data has been written to 'data/adults.csv'.")
