import numpy as np
        

def calculate_joltage(line, size):
    sol = ''
    eliminate = len(line)-size
    while eliminate>0 and len(sol)<size:
        digits = np.array([int(c) for c in line])
        pos = int(np.argmax(digits[:eliminate+1]))
        sol += line[pos]
        line = line[pos+1:]
        eliminate -= pos
    if len(sol)<size:
        sol += line
    return int(sol)
        

# Variables definition
file_path = "./data/day_3.in"
count_1 = 0
count_2 = 0

# Data parsing
with open(file_path, "r") as f:
    data = [line.strip() for line in f]

for line in data:
    # Parte 1
    count_1 += calculate_joltage(line, 2)

    # Parte 2
    count_2 += calculate_joltage(line, 12)


# Show answers
print(f'Part 1: {count_1}')
print(f'Part 2: {count_2}')