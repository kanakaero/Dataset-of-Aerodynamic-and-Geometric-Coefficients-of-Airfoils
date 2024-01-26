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

with open('logOpt.txt', 'r') as log_file:
    log_lines = log_file.readlines()

cl, cd = extract_values(log_lines)

output_csv_path = 'Results.csv'
write_header = not os.path.exists(output_csv_path)  # Check if the CSV file exists

with open(output_csv_path, 'a', newline='') as output_csv:
    csv_writer = csv.writer(output_csv)
    if write_header:
        header_row = ['Filename', 'AoA'] + [f'CST Coeff {i}' for i in range(1, 9)] + ['Cl', 'Cd']]
        csv_writer.writerow(header_row)
    csv_writer.writerow([dat_filename, aoa] + coeff_data + [cl, cd])

print(f"Values extracted and saved to Results.csv for {dat_filename}")
