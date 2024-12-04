import random

def uvod():
    print("Vítejte ve hře 'Panna nebo Orel'!")
    print("Pravidla jsou jednoduchá: hodíme mincí a uvidíme, co padne.")
    print("-" * 40)

def hod_mince():
    print("Házím mincí...")
    vysledek = random.choice(["Panna", "Orel"])
    return vysledek

def zobrazeni_vysledku(vysledek):
    print(f"Výsledek hodu: {vysledek}")
    if vysledek == "Panna":
        print("Padla panna, gratulace!")
    else:
        print("Padl orel, paráda!")

def chce_pokracovat():
    odpoved = input("Chcete hodit znovu? (ano/ne): ").strip().lower()
    return odpoved in ["ano", "a", "jo"]

def hra():
    uvod()
    pokracovat = True
    while pokracovat:
        vysledek = hod_mince()
        zobrazeni_vysledku(vysledek)
        pokracovat = chce_pokracovat()
    print("Díky za hru!")

hra()
