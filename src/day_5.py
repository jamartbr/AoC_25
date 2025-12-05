file_path = "./data/day_5.in"

with open(file_path) as f:
    ranges, ids = f.read().strip().split('\n\n')
ranges = [tuple(map(int, line.split('-'))) for line in ranges.splitlines()]
ids = [int(x) for x in ids.splitlines()]

# Part 1
count_1 = sum(1 for id in ids if any(a<=id<= b for a,b in ranges))

# Part 2
ranges.sort()
merged = []
for a, b in ranges:
    if not merged or a > merged[-1][1]:
        merged.append([a, b])
    else:
        merged[-1][1] = max(merged[-1][1],b)
count_2 = sum(b-a+1 for a,b in merged)

print(f'Part 1: {count_1}')
print(f'Part 2: {count_2}')
