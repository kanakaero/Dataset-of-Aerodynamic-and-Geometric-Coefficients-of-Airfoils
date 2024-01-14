#!/bin/bash

# Run simulations in parallel using a loop
for dir in pc1 pc2 pc3 pcN; do # depends on the number of subdirectories
    (cd "$dir" && pwd && nohup ./AllRun.sh 0</dev/null 1> sim.out 2>sim.err) &
done

# Wait for all background processes to finish
wait
