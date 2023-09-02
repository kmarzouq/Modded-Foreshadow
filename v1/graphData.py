import matplotlib.pyplot as plt
import re

datx=[]
daty=[]

goodx=[]
goody=[]

def find_integer_in_line(line):
    # Regular expression pattern to find an integer
    pattern = r'\b\d+\b'
    
    # Search for the pattern in the line
    match = re.search(pattern, line)
    
    if match:
        return int(match.group())
    else:
        return None

# Open the file in read mode
with open("allBytes.txt", "r") as file:
    # Read each line from the file
    for line in file:
        # Split the line into words
        words = line.split()
        
        if "byte" in line:
            datx.append(find_integer_in_line(line))
        elif "access time" in line:
            daty.append(find_integer_in_line(line))

# Open the file in read mode
with open("allBytesGood.txt", "r") as file:
    # Read each line from the file
    for line in file:
        # Split the line into words
        words = line.split()
        
        if "byte" in line:
            goodx.append(find_integer_in_line(line))
        elif "access time" in line:
            goody.append(find_integer_in_line(line))


plt.scatter(datx, daty, color='blue', label='All data')
plt.scatter(goodx, goody, color='green', label = 'Successful data')
plt.xlabel("byte number")
plt.ylabel("Access time for each bytes")
plt.ylim(0,200)
plt.show()
