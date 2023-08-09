"""
Reads data from "data.csv" and writes filtered data to "adults.csv".
"""

import csv

def filter_adults(input_filename, output_filename):
    """
    Filter and write data of adults from the input file to the output file.
    """
    with open(input_filename, 'r', newline='', encoding='utf-8') as input_file, \
            open(output_filename, 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:
            age = int(row['Age'])  # Convert the 'Age' value to an integer
            if age >= 18:  # Check if the age is 18 or older
                writer.writerow(row)  # Write the row to the output file

if __name__ == "__main__":
    INPUT_FILENAME = 'data/data.csv'
    OUTPUT_FILENAME = 'data/adults.csv'
    filter_adults(INPUT_FILENAME, OUTPUT_FILENAME)
    print("Filtered data has been written to 'data/adults.csv'.")
