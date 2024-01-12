import os
import pandas as pd

def concatenate_results_csv(input_folder, output_file):
    # Get a list of all subdirectories (pc folders)
    subdirectories = [subdir for subdir in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, subdir))]

    # Check if there are any subdirectories
    if not subdirectories:
        print("No subdirectories found in the input folder.")
        return

    # Read the header of the first Results.csv file
    first_file_path = os.path.join(input_folder, subdirectories[0], 'Results.csv')
    first_file_header = pd.read_csv(first_file_path, nrows=0).columns.tolist()

    # Create an empty DataFrame to store the concatenated data
    concatenated_data = pd.DataFrame(columns=first_file_header)

    # Concatenate the data from all Results.csv files
    for subdir in subdirectories:
        file_path = os.path.join(input_folder, subdir, 'Results.csv')
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            concatenated_data = pd.concat([concatenated_data, df], ignore_index=True)

    # Write the concatenated data to a new CSV file
    concatenated_data.to_csv(output_file, index=False)
    print(f"Concatenated data saved to {output_file}")

# Example usage:
input_folder = '.'
output_file = './Results_AoA_0.csv' # the corresponding AoA
concatenate_results_csv(input_folder, output_file)

