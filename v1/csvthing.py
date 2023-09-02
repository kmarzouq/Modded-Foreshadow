import re
import csv
context_switches=[]                           
cpu_migrations=[] 
page_faults=[]                  
cycles=[]                                    
instructions=[]                       
branches=[]                             
branch_misses=[]                     
seconds_time_elapsed=[]
seconds_user=[]
seconds_sys=[]

csv_file_name = 'output_dat.csv'

# Open the text file for reading
with open('logPerf.txt', 'r') as file:
    # Read the content of the file
    for line in file:
        numbers_with_commas = re.findall(r'\d+(?:,\d+)*(?:\.\d+)?', line)
        numbers_without_commas = [float(number.replace(',', '')) for number in numbers_with_commas]
        if "context" in line:
            context_switches.append(numbers_without_commas[0])
        if "migrations" in line:
            cpu_migrations.append(numbers_without_commas[0])
        if "page" in line:
            page_faults.append(numbers_without_commas[0])
        if "cycles" in line:
            cycles.append(numbers_without_commas[0])
        if "instructions" in line:
            instructions.append(numbers_without_commas[0])
        if "branches" in line:
            branches.append(numbers_without_commas[0])
        if "misses" in line:
            branch_misses.append(numbers_without_commas[0])
        if "elapsed" in line:
            seconds_time_elapsed.append(numbers_without_commas[0])
        if "user" in line:
            seconds_user.append(numbers_without_commas[0])
        if "sys" in line:
            seconds_sys.append(numbers_without_commas[0])

# Use regular expressions to find all numbers with commas
# and convert them to numbers without commas


with open(csv_file_name, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    csv_writer.writerow(['context_switches', 'cpu_migrations', 'page_faults','cycles','instructions', 'branches', 'branch_misses','seconds_time_elapsed','seconds_user','seconds_sys'])
    for i in range(len(cycles)):
        csv_writer.writerow([context_switches[i], cpu_migrations[i], page_faults[i], cycles[i], instructions[i],branches[i],branch_misses[i],seconds_time_elapsed[i], seconds_user[i],seconds_sys[i]])

print(f'CSV file "{csv_file_name}" created successfully.')
