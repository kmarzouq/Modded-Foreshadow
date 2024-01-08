#!/bin/bash

# Number of times to run the program
num_runs=10



# Loop to run the program multiple times
for ((i=1; i<=$num_runs; i++))
do
    bash run_command.sh 
    #python3 analyze2.py | tee -a log.txt
    python3 run.py
done
