import random
import time
import os

# Získáme velikost okna terminálu
columns, rows = os.get_terminal_size()

chars = "0123456789ABCDEFHIJKLMNOPQRSTUVWXYZ$#@&"
# Seznam pro uložení aktuální pozice "kapek" v každém sloupci
drops = [0] * columns

print("\033[32m") # Nastaví barvu na zelenou

while True:
    for i in range(len(drops)):
        char = random.choice(chars)
        # Pokud je drop > 0, vypíšeme znak, jinak mezeru
        if random.random() > 0.95:
            drops[i] = 1
        
        if drops[i] > 0:
            print(char, end="")
            drops[i] += 1
            if drops[i] > rows or random.random() > 0.95:
                drops[i] = 0
        else:
            print(" ", end="")
            
    print()
    time.sleep(0.05)
