#Vytvořte 6 proměnných number1 až number6. Do každé proměnné uložíte výsledek hodu kostkou - tedy číslo od 1 do 6. Poté do proměnné sum všech 6 čísel nasčítáte a pokud je součet větší nebo rovno 25, tak vypíšete "Vítěz". Pokud menší, tak "Zkus znovu své štěstí". Na vhodném místě také do konzole vypíšete celkový součet všech 6 čísel.
 

import random

number1 = random.randint(1, 6)
number2 = random.randint(1, 6)
number3 = random.randint(1, 6)
number4 = random.randint(1, 6)
number5 = random.randint(1, 6)
number6 = random.randint(1, 6)

sum_numbers = number1 + number2 + number3 + number4 + number5 + number6

print(f"Součet je: {sum_numbers}")

if sum_numbers >= 25:
    print("Vítěz")
else:
    print("Zkus znovu své štěstí")
