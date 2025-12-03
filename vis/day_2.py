import re
import time

# --- Definiciones de Color ANSI ---
COLOR_BLANCO = "\033[97m" # Color inicial
COLOR_ROJO = "\033[91m"  # Color rojo
COLOR_VERDE = "\033[92m"  # Color de selección
COLOR_TERMINAL = "\033[0m" # Restablecer
PAUSA = 0.01  # Pausa en segundos entre pasos
LINE_UP = '\033[1A'
LINE_CLEAR = '\033[K'

# Variables definition
file_path = "./data/test_2.in"
count_1 = 0
count_2 = 0

# Data parsing
with open(file_path, "r") as f:
    data = [l.split('-') for l in f.readline().split(',')]

# Parte 1
print(f'{COLOR_TERMINAL}Procesando primer problema')
for start, stop in data:
    for i in range(int(start), int(stop)+1):
        print(f"{COLOR_BLANCO}{i}")
        time.sleep(PAUSA)

        c = str(i)
        half = len(c)//2

        if len(c)%2==0 and c[:half]==c[half:]:
            count_1 += i
            print(f"{LINE_UP}{LINE_CLEAR}{COLOR_ROJO}{i}{COLOR_BLANCO}")
            time.sleep(PAUSA)
        else:
            print(f"{LINE_UP}{LINE_CLEAR}{COLOR_VERDE}{i}{COLOR_BLANCO}")
            time.sleep(PAUSA)
            print(f"{LINE_UP}{LINE_CLEAR}{LINE_UP}")
            time.sleep(PAUSA)
print(f'{COLOR_TERMINAL}Se ha terminado de procesar el primer problema')

# Parte 2
print(f'{COLOR_TERMINAL}Procesando segundo problema')
for start, stop in data:
    for i in range(int(start), int(stop)+1):
        print(f"{COLOR_BLANCO}{i}")
        time.sleep(PAUSA)

        c = str(i)
        half = len(c)//2
        valid = True
        
        for j in range(1,half+1):
            if len(c)/j==len(re.findall(c[:j], c)):
                count_2 += i
                valid = False
                
                break
        if not valid:
            print(f"{LINE_UP}{LINE_CLEAR}{COLOR_ROJO}{i}{COLOR_BLANCO}")
        else:
            print(f"{LINE_UP}{LINE_CLEAR}{COLOR_VERDE}{i}{COLOR_BLANCO}")
            time.sleep(PAUSA)
            print(f"{LINE_UP}{LINE_CLEAR}{LINE_UP}")
            time.sleep(PAUSA)
print(f'{COLOR_TERMINAL}Se ha terminado de procesar el segundo problema')


# Show answers
print(f'{COLOR_TERMINAL}Part 1: {count_1}')
print(f'{COLOR_TERMINAL}Part 2: {count_2}')