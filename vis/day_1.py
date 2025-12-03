import math
import matplotlib.pyplot as plt

file_path = "./data/test_1.in"

# Parse data
with open(file_path, "r") as f:
    data = [[line[0], int(line[1:])] for line in f]

def coord(n, radius=1.0):
    # Place 0 at top and numbers increase clockwise
    angle = math.pi/2 - 2*math.pi*(n/100.0)
    return radius * math.cos(angle), radius * math.sin(angle)

# Draw dial
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect("equal")
ax.axis("off")

# Circle and ticks
circle = plt.Circle((0,0), 1.0, fill=False, linewidth=2)
ax.add_artist(circle)

# Label every 5
for n in range(0, 100, 5):
    x, y = coord(n, 1.06)
    ax.text(x, y, str(n), ha="center", va="center", fontsize=8)

# Pointer (line from center to number)
current = 50
px, py = coord(current)
pointer_line, = ax.plot([0, px], [0, py], color="red", linewidth=3, marker="o")

# Status text
count_1 = 0
count_2 = 0
status = ax.text(-1.0, -1.5, f"stops at zero: {count_1}\nzero crossings: {count_2}", fontsize=12)

ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
plt.ion()
plt.show()

# Animate moves
for direction, orig_value in data:
    count_2 += orig_value // 100
    value = orig_value % 100
    status.set_text(f"rotation: {direction}{orig_value}\nstops at zero: {count_1}\nzero crossings: {count_2}")

    # step one unit at a time to visualize crossing 0
    prev = current
    steps = range(1, value + 1)
    for s in steps:
        if direction == 'L':
            new_pos = (current - 1) % 100
        else:
            new_pos = (current + 1) % 100

        # detect crossing of 0 exactly as the step-by-step equivalent:
        # if we moved onto 0 from a non-zero position, that's a crossing.
        if prev != 0 and new_pos == 0:
            count_2 += 1
            status.set_text(f"rotation: {direction}{orig_value}\nstops at zero: {count_1}\nzero crossings: {count_2}")

        # update pointer
        x, y = coord(new_pos)
        pointer_line.set_data([0, x], [0, y])
        fig.canvas.draw()
        plt.pause(1e-10)

        prev = new_pos
        current = new_pos
    
    count_1 += current==0

# final print
print(f'Part 1: {count_1}')
print(f'Part 2: {count_2}')
# keep window open
plt.ioff()
plt.show()
