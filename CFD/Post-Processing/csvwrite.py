import os
import re
import sys
import csv

datfiles_folder = sys.argv[1]

coeff_data = sys.argv[2].split()
aoa = 0

# Extract the filename from the command line argument and remove the ".dat" extension
dat_filename = os.path.splitext(sys.argv[3])[0]

dat_file_path = os.path.join(datfiles_folder, f'{dat_filename}.dat')

def extract_values(log_lines):
    cl = None
    cd = None
    for line in log_lines:
        if "Cd:" in line:
            cd = float(re.findall(r"Cd:\s+([-.\d]+)", line)[0])
        if "Cl:" in line:
            cl = float(re.findall(r"Cl:\s+([-.\d]+)", line)[0])
    return cl, cd

def read_dat_file(dat_file_path):
    coordinates = []
    with open(dat_file_path, 'r') as dat_file:
        for line in dat_file:
            # Assuming the coordinates are space-separated on each line
            # If the format is different, adjust the parsing logic accordingly
            x, y = map(float, line.split())
            coordinates.append((x, y))
    return coordinates

with open('logOpt.txt', 'r') as log_file:
    log_lines = log_file.readlines()

cl, cd = extract_values(log_lines)

# Read the 600-point coordinate pairs from the .dat file
#coordinates = read_dat_file(dat_file_path)


output_csv_path = 'Results.csv'
write_header = not os.path.exists(output_csv_path)  # Check if the CSV file exists

with open(output_csv_path, 'a', newline='') as output_csv:
    csv_writer = csv.writer(output_csv)
    if write_header:
        #header_row = ['Filename', 'AoA'] + [f'CST Coeff {i}' for i in range(1, 9)] + ['Cl', 'Cd'] + [f'Coordinate {i}' for i in range(1, 601)]
        header_row = ['Filename', 'AoA'] + [f'CST Coeff {i}' for i in range(1, 9)] + ['Cl', 'Cd']]
        csv_writer.writerow(header_row)
    # Convert the coordinate pairs to a list of strings
    coordinates_list = [f'{x},{y}' for x, y in coordinates]
    csv_writer.writerow([dat_filename, aoa] + coeff_data + [cl, cd] + coordinates_list)

print(f"Values extracted and saved to Results.csv for {dat_filename}")
