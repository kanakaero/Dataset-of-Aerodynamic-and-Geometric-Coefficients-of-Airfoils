#!/bin/bash

# Run simulations in parallel using a loop
for dir in pc*; do
    (cd "$dir" && pwd && nohup ./AllRun.sh 0</dev/null 1> sim.out 2>sim.err) &
done

# Wait for all background processes to finish
wait
