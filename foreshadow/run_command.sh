#!/bin/bash

# Number of times to run the program
num_runs=20



# Loop to run the program multiple times
for ((i=1; i<=$num_runs; i++))
do
    make run
done
