# Vytvořte proměnnou passwords (pole) a uložte do ní tři stringy - texty (i text může mít v sobě čísla). 
# Vaším úkolem je náhodně vybrat jedno heslo. 
# Při každém znovunačtení stránky se do konzole vypíše jedno ze tří hesel (náhodně).


import random

passwords = ["46133ewds", "admin255dd", "TádaJeCool1235"]

random_number = random.randint(1, 3)
index = len(passwords) - random_number

print(passwords[index])
