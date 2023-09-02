#!/bin/bash

# Number of times to run the program
num_runs=200



# Loop to run the program multiple times
for ((i=1; i<=$num_runs; i++))
do
    perf stat make run 2>&1 | tee -a output.txt

done
python3 analyze2.py
