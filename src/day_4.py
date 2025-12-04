# Variables definition
file_path = "./data/day_4.in"
count_1 = 0
count_2 = 0
neigh = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if not (dx == 0 and dy == 0)]

def surrounding_rolls(i, j):
    return sum(
        0 <= i + dx < len(data) and 0 <= j + dy < len(data[0]) and data[i + dx][j + dy] == '@'
        for dx, dy in neigh
    )

# Data parsing
with open(file_path) as f:
    data = [list(line.strip()) for line in f]

# Part 1
count_1 = sum(1 for i, row in enumerate(data) for j, c in enumerate(row) if c == '@' and surrounding_rolls(i, j) < 4)

# Part 2
while True:
    remove = [(i, j) for i, row in enumerate(data) for j, c in enumerate(row) if c == '@' and surrounding_rolls(i, j) < 4]
    if not remove:
        break
    count_2 += len(remove)
    for i, j in remove:
        data[i][j] = '.'

# Show answers
print(f'Part 1: {count_1}')
print(f'Part 2: {count_2}')
