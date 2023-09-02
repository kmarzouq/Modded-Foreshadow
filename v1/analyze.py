# Open the output.txt file for reading
with open('output.txt', 'r') as file:
    lines = file.readlines()

# Initialize variables
counter = 0
found_marker = False
ast=0
zer=0
ff=0

# Loop through each line in the file
for line in lines:
    if "shadow" in line and "enclave" in line and ";" in line:
        ast = line.count('**')
        zer = line.count('0x00')
        ff  = line.count('0xff') 
        counter = counter + (2-ast)
        ast=0;

# Print the total count
print("Total count of valid sets:", counter)
