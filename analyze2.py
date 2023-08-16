import re

# Open the output.txt file for reading
with open('output.txt', 'r') as file:
    lines = file.readlines()


def extract_hex_values(line):
    hex_values = re.findall(r'0x[0-9a-fA-F]+', line)
    return hex_values

# Initialize variables
counter = 0
found_marker = False
ast=0
zer=0
ff=0
no=False

# Loop through each line in the file
for line in lines:
    if "shadow" in line and "enclave" in line and ";" in line:
        ast = line.count('**')
        if (ast<2):
            use1=extract_hex_values(line)
            if use1[0]==use1[1]:
                if use1[0]!='0x00' and use1[0]!='0xff':
                    if use1[0][2]!='0':
                        counter=counter+1
            if use1[2]==use1[3]:
                if use1[2]!='0x00' and use1[2]!='0xff':
                    if use1[2][2]!='0':
                        counter=counter+1
            

# Print the total count
print("Total count of valid sets:", counter)
