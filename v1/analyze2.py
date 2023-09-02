import re

# Open the output.txt file for reading
with open('output.txt', 'r') as file:
    lines = file.readlines()

def find_integer_in_line(line):
    # Regular expression pattern to find an integer
    pattern = r'\b\d+\b'
    
    # Search for the pattern in the line
    match = re.search(pattern, line)
    
    if match:
        return int(match.group())
    else:
        return None

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
temp=0
bitter = [0]*64
avg=[0]*200
avg2=[]
ktr=0;
wb=0;
good=0;

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
                        avg2.append(bitter[wb])
                        with open('allBytesGood.txt','a') as target:
                            sleep = "byte:" + str(wb) + "\n access time: " + str(bitter[wb]) + "\n"
                            target.write(sleep)
                        with open('logPerf.txt','a') as target:
                            target.write(line)
                        with open('logPerfGood.txt','a') as target:
                            target.write("byte "+str(wb)+'\n')
                        good=1

            if use1[2]==use1[3]:
                if use1[2]!='0x00' and use1[2]!='0xff':
                    if use1[2][2]!='0':
                        counter=counter+1
                        avg2.append(bitter[wb+1])
                        with open('allBytesGood.txt','a') as target:
                            sleep = "byte:" + str(wb+1) + "\n access time: " + str(bitter[wb+1]) + "\n"
                            target.write(sleep)
                        with open('logPerf.txt','a') as target:
                            target.write(line)
                        with open('logPerfGood.txt','a') as target:
                            target.write("byte " + str(wb+1)+'\n')
                        good=1
        wb+=2
    elif "main.c" in line and "byte" in line:
        temp=find_integer_in_line(line)
        good=0

    elif "foreshadow.c" in line and "access time is" in line:
        bitter[temp]=find_integer_in_line(line)
        with open('allBytes.txt','a') as target:
            catb="byte:" + str(temp) + "\n"
            cata="access time is:" + str(bitter[temp]) + "\n\n"
            target.write(catb)
            target.write(cata)

    elif "bytes out of" in line:
        avg[ktr]=sum(bitter)/len(bitter)
        for i in bitter:
            i=0
        ktr+=1;
        wb=0;
        with open('logPerf.txt','a') as target:
            text = "\n run " + str(ktr) + "\n"
            target.write(text)
    elif counter>0 and "task-clock" in line or "context-switches" in line or "cpu-migrations" in line or "page-faults" in line or "cycles" in line or "instructions" in line or "branches" in line or "branch-misses" in line or "seconds time elapsed" in line or "seconds user" in line or "seconds sys" in line:
        with open('logPerf.txt','a') as target:
            target.write(line)
        if good==1:
            with open('logPerfGood.txt','a') as target:
                target.write(line)
        


print("\nTotal count of valid sets:",counter, "\n count is this:", ktr)
print("average access time is ", int(sum(avg)/len(avg)))
print(" which is ", avg)
print("average successful access time is ", int(sum(avg2)/len(avg2)))
print(" which is ",avg2)
