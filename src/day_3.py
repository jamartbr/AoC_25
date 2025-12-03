import numpy as np
        

# Variables definition
file_path = "./data/day_3.in"
count_1 = 0
count_2 = 0

# Data parsing
with open(file_path, "r") as f:
    data = [line.strip() for line in f]

for line in data:
    digits = np.array([int(c) for c in line])

    # Parte 1
    pos = int(np.argmax(digits[:-1]))
    count_1 += digits[pos] * 10 + digits[pos+1:].max()

    # Parte 2
    sol = ''
    eliminate = len(line)-12
    while eliminate>0 and len(sol)<12:
        pos = int(np.argmax(digits[:eliminate+1]))
        sol += line[pos]
        line = line[pos+1:]
        eliminate -= pos
        digits = np.array([int(c) for c in line])
    if len(sol)<12:
        sol += line
    count_2 += int(sol)


# Show answers
print(f'Part 1: {count_1}')
print(f'Part 2: {count_2}')