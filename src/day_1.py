# Variables definition
file_path = "./data/day_1.in"
current = 50
count_1 = 0
count_2 = 0

# Data parsing
with open(file_path, "r") as f:
    data = [[line[0], int(line[1:])] for line in f]

# Problems resolution
for direction, value in data:
    # Part 1
    count_1 += int(current==0)

    # Part 2
    count_2 += value // 100
    value %= 100
    if direction=='L':
        count_2 += int(current and value>=current)
        current = (current - value) % 100
    else:
        count_2 += int(current and value>=(100-current))
        current = (current + value) % 100

# Show answers
print(f'Part 1: {count_1}')
print(f'Part 2: {count_2}')

