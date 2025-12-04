import time
import os

# --- Definiciones de Color ANSI ---
COLOR_BLANCO = "\033[97m" # Color inicial
COLOR_VERDE = "\033[92m"  # Color de selección
COLOR_TERMINAL = "\033[0m" # Restablecer
COLOR_GRIS = "\033[90m"   # Para "desaparecer" (hacer tenue)
PAUSA = 0.5  # Pausa en segundos entre pasos
LINE_UP = '\033[1A'
LINE_CLEAR = '\033[K'

def show(data):
    os.system('clear')
    out = ''
    for line in data:
        out += COLOR_TERMINAL.join(line) + '\n'
    print(out)
    time.sleep(PAUSA)

def show_select(data, pos):
    os.system('clear')
    out = ''
    for i,line in enumerate(data):
        for j,char in enumerate(line):
            if (i,j) in pos:
                # Pone el dígito seleccionado en VERDE
                out += f"{COLOR_VERDE}{char}"
            else:
                # Los no seleccionados quedan en gris
                out += f"{COLOR_GRIS}{char}"
        out += '\n'
    print(out)
    time.sleep(PAUSA)

def surrounding_rolls(i, j):
    return sum(
        0 <= i + dx < len(data) and 0 <= j + dy < len(data[0]) and data[i + dx][j + dy] == '@'
        for dx, dy in neigh
    )

# Variables definition
file_path = "./data/day_4.in"
count_1 = 0
count_2 = 0
neigh = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if not (dx == 0 and dy == 0)]


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
    show_select(data,remove)
    for i, j in remove:
        data[i][j] = '.'
    show(data)

# Show answers
print(f'{COLOR_TERMINAL}Part 1: {count_1}')
print(f'{COLOR_TERMINAL}Part 2: {count_2}')
