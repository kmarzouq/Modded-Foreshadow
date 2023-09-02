import matplotlib.pyplot as plt
import re

datx=[]
daty=[]

goodx=[]
goody=[]

plus=0

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
with open("logPerf.txt", "r") as file:
    # Read each line from the file
    for line in file:
        # Split the line into words
        words = line.split()
        
        if "run" in line:
            datx.append(find_integer_in_line(line))
        elif "branches" in line:
            daty.append(find_integer_in_line(line))

# Open the file in read mode
with open("logPerfGood.txt", "r") as file:
    # Read each line from the file
    for line in file:
        # Split the line into words
        words = line.split()

        if "branches" in line:
            plus=(plus+1)%201;
            goodx.append(plus)
            goody.append(find_integer_in_line(line))

print(datx)
print(daty)

plt.scatter(datx, daty, color='blue', label='All data')
plt.scatter(goodx, goody, color='green', label = 'Successful data')
plt.xlabel("run number")
plt.ylabel("branches for each leak")
plt.show()
