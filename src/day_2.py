import re

# Variables definition
file_path = "./data/day_2.in"
count_1 = 0
count_2 = 0

# Data parsing
with open(file_path, "r") as f:
    data = [l.split('-') for l in f.readline().split(',')]

# Problems resolution
for start, stop in data:
    for i in range(int(start), int(stop)+1):
        c = str(i)
        half = len(c)//2

        # Part 1
        if len(c)%2==0 and c[:half]==c[half:]:
            count_1 += i
    
        # Part 2
        for j in range(1,half+1):
            if len(c)/j==len(re.findall(c[:j], c)):
                count_2 += i
                break


# Show answers
print(f'Part 1: {count_1}')
print(f'Part 2: {count_2}')

