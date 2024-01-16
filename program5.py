# Vytvořte hru Panna nebo Orel. Importujte modul random:


import random
 
side_coin = random.randint(0,1)
if side_coin == 0:
    print("Panna")
else:
    print("Orel")
