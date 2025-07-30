import time
import os

try:
    from colorama import init, Fore
    init()
    COLOR_ENABLED = True
except ImportError:
    COLOR_ENABLED = False  

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{mins:02}:{secs:02}"

def countdown(seconds):
    clear()
    print("Spouštím odpočet...\n")
    for i in range(seconds, 0, -1):
        time_str = format_time(i)
        color = Fore.CYAN if COLOR_ENABLED else ""
        reset = Fore.RESET if COLOR_ENABLED else ""
        print(f"{color}Odpočet: {time_str}{reset}", end='\r')
        time.sleep(1)
    print("\n Stratil jsi 1 minutu svého života :) \n")

# Nastav délku odpočtu v sekundách (např. 120 = 2 minuty)
countdown(60)
