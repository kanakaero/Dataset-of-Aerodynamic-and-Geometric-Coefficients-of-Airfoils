import csv
import os

# Function to read coefficients from the Filename_Coeffs.txt file
def read_coefficients(filename):
    coeffs = []
    with open(os.path.join('', filename + '_Coeffs.txt'), 'r') as coeff_file:
        for line in coeff_file:
            # Split the line into individual coefficients and store them as strings
            coefficients = line.strip().split()
            coeffs.extend(coefficients)  # Extend the list with coefficients
    return coeffs

# Open the CSV file for reading
with open('', 'r', newline='') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Skip the header row
    data = list(reader)

# Update the header to include CST coefficients
header[2:2] = ['CST Coeff 1', 'CST Coeff 2', 'CST Coeff 3', 'CST Coeff 4', 'CST Coeff 5', 'CST Coeff 6', 'CST Coeff 7', 'CST Coeff 8']

# Initialize a list to store the modified data
modified_data = []

# Add CST coefficients to each row
for row in data:
    filename = row[0]  # airfoil name is in the first column
    cl = row[2]
    cd = row[3]
    coeffs = read_coefficients(filename)
    # Initialize a list to store the modified row
    modified_row = [0] * 12  # Initialize with 12 elements
    # Insert values into the modified row
    modified_row[0] = row[0]  # Airfoil name
    modified_row[1] = row[1]  # AoA
    modified_row[2:10] = coeffs[:8]  # CST coefficients
    modified_row[10] = cl  # Cl
    modified_row[11] = cd  # Cd
    # Append the modified row to the list of modified data
    modified_data.append(modified_row)

# Write the modified data back to the CSV file
with open('', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(modified_data)
