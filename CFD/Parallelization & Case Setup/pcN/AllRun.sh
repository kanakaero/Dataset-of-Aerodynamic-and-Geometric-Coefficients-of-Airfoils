#!/bin/bash
datfiles_folder="./DAT_FILES_COEFFS"    # put the path where the dat files are stored
case_directory="."  # put the path of the case
i=1
for dat_file in "$datfiles_folder"/*.dat; do
    if [ -f "$dat_file" ]; then
        dat_filename=$(basename "$dat_file")
        cp "$dat_file" "$case_directory/datfile.dat"
        echo "Running automesher.py..."
        cd "$case_directory"
        python3 automesh.py # Mesh Generation

        echo "Running Simulation..."
        # Setting up the Case
        rm -rf 0
        rm -rf postProcessing
        rm -rf constant/polyMesh/
        rm -rf logOpt.txt
        rm -rf *.bin *.info *.dat *.xyz *.stl
        rm -rf 2000
        rm -rf sim.out
        rm -rf sim.err
        # Copying 0 file
        mkdir 0/
        cp 0.orig/* 0/
        # blockMesh and simpleFoam
        blockMesh # generate the mesh
        simpleFoam | tee logOpt.txt #run in parallel

        echo "Processed: $dat_filename"

        # Form the coefficient file name
        coeff_file="$datfiles_folder/${dat_filename%.*}_Coeffs.txt"
        # Extract coefficient data
        if [ -f "$coeff_file" ]; then
            coeff_data=$(cat "$coeff_file")
        else
            coeff_data=""
        fi
        python3 output.py "$datfiles_folder" "$coeff_data" "$dat_filename" #Pass the necessary parameters here
        echo "$i Processed: $dat_filename" >> datfilesdone.txt
    else
      echo "Not working"
    fi
    ((i++))
done
