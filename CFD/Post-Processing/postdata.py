import csv
import os

# Function to read coefficients from the Filename_Coeffs.txt file
def read_coefficients(filename):
    coeffs = []
    with open(os.path.join('', filename + '_Coeffs.txt'), 'r') as coeff_file: # path to coeff files
        for line in coeff_file:
            # Split the line into individual coefficients and store them as strings
            coefficients = line.strip().split()
            coeffs.extend(coefficients)  # Extend the list with coefficients
    return coeffs

# Open the CSV file for reading
with open('', 'r', newline='') as infile: # path to .csv file
    reader = csv.reader(infile)
    header = next(reader)  # Skip the header row
    data = list(reader)

# Update the header to include CST coefficients
header[2:2] = ['CST Coeff 1', 'CST Coeff 2', 'CST Coeff 3', 'CST Coeff 4', 'CST Coeff 5', 'CST Coeff 6', 'CST Coeff 7', 'CST Coeff 8']

# Add CST coefficients to each row
for row in data:
    filename = row[0]  # airfoil name is in the first column
    coeffs = read_coefficients(filename)
    # Insert CST coefficients between AoA and Cl columns
    row[2:10] = coeffs[:8]  # Assuming you have 8 coefficients

# Write the modified data back to the CSV file
with open('', 'w', newline='') as outfile: # final .csv filename
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(data)

