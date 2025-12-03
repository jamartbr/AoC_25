import numpy as np
import time

# --- Definiciones de Color ANSI ---
COLOR_BLANCO = "\033[97m" # Color inicial
COLOR_VERDE = "\033[92m"  # Color de selección
COLOR_TERMINAL = "\033[0m" # Restablecer
COLOR_GRIS = "\033[90m"   # Para "desaparecer" (hacer tenue)
PAUSA = 0.01  # Pausa en segundos entre pasos
LINE_UP = '\033[1A'
LINE_CLEAR = '\033[K'

def show_select(line, sol):
    out = ''
    k=0
    for char in line:
        if k<len(sol) and char == sol[k]:
            # Pone el dígito seleccionado en VERDE
            out += f"{COLOR_VERDE}{char}{COLOR_BLANCO}"
            k += 1
        else:
            # Los no seleccionados quedan en gris
            out += f"{COLOR_GRIS}{char}"
    return out

def calculate_joltage(line, size):
    print(f"{COLOR_BLANCO}{line}")
    time.sleep(PAUSA)

    orig = line
    sol = ''
    eliminate = len(line)-size
    selected = []
    while eliminate>0 and len(sol)<size:
        digits = np.array([int(c) for c in line])
        pos = int(np.argmax(digits[:eliminate+1]))
        sol += line[pos]
        line = line[pos+1:]
        eliminate -= pos
    if len(sol)<size:
        sol += line

    print(f"{LINE_UP}{LINE_CLEAR}{show_select(orig, sol)}")
    time.sleep(PAUSA)

    return int(sol)
        

# Variables definition
file_path = "./data/test_3.in"
count_1 = 0
count_2 = 0

# Data parsing
with open(file_path, "r") as f:
    data = [line.strip() for line in f]

# Parte 1
print(f'{COLOR_TERMINAL}Procesando primer problema')
for line in data:
    count_1 += calculate_joltage(line, 2)
print(f'{COLOR_TERMINAL}Se ha terminado de procesar el primer problema')

# Parte 2
print(f'{COLOR_TERMINAL}Procesando segundo problema')
for line in data:
    count_2 += calculate_joltage(line, 12)
print(f'{COLOR_TERMINAL}Se ha terminado de procesar el segundo problema')

# Show answers
print(f'{COLOR_TERMINAL}Part 1: {count_1}')
print(f'{COLOR_TERMINAL}Part 2: {count_2}')