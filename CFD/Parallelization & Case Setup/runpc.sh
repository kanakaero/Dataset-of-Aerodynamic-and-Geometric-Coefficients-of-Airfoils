#!/bin/bash

# Run simulations in parallel using a loop
for dir in pc1 pc2 pc3 pc4 pc5 pc6 pc7 pc8 pc9 pc10 pc11 pc12 pc13 pc14 pc15 pc16 pc17 pc18 pc19 pc20 pc21 pc22 pc23 pc24 pc25 pc26 pc27 pc28 pc29 pc30 pc31 pc32 pc33 pc34 pc35 pc36 pc37 pc38 pc39 pc40 pc41 pc42 pc43 pc44 pc45 pc46 pc47 pc48 pc49 pc50 pc51 pc52 pc53 pc54 pc55 pc56 pc57 pc58 pc59 pc60; do
    (cd "$dir" && pwd && nohup ./AllRun.sh 0</dev/null 1> sim.out 2>sim.err) &
done

# Wait for all background processes to finish
wait
