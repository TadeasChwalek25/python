def kalkulacka():
    print("Jednoduchá kalkulačka")
    print("Vyber operaci:")
    print("1. Sčítání")
    print("2. Odčítání")
    print("3. Násobení")
    print("4. Dělení")
    
    # Výběr operace
    operace = input("Zadej číslo operace (1/2/3/4): ")

    # Zadání čísel
    try:
        cislo1 = float(input("Zadej první číslo: "))
        cislo2 = float(input("Zadej druhé číslo: "))
    except ValueError:
        print("Neplatný vstup, zadejte čísla.")
        return
    
    # Výpočet podle vybrané operace
    if operace == '1':
        vysledek = cislo1 + cislo2
        print(f"{cislo1} + {cislo2} = {vysledek}")
    elif operace == '2':
        vysledek = cislo1 - cislo2
        print(f"{cislo1} - {cislo2} = {vysledek}")
    elif operace == '3':
        vysledek = cislo1 * cislo2
        print(f"{cislo1} * {cislo2} = {vysledek}")
    elif operace == '4':
        if cislo2 == 0:
            print("Chyba: Dělení nulou není povoleno.")
        else:
            vysledek = cislo1 / cislo2
            print(f"{cislo1} / {cislo2} = {vysledek}")
    else:
        print("Neplatná operace.")

# Spuštění kalkulačky
kalkulacka()
