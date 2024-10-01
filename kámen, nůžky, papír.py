import random

def hra_kamen_nuzky_papir():
    print("Vítej ve hře Kámen, nůžky, papír!")
    vybery = ["kámen", "nůžky", "papír"]
    
    while True:
        # Hráčův výběr
        hracuv_vyber = input("Vyber si: kámen, nůžky, nebo papír (nebo 'konec' pro ukončení): ").lower()
        
        if hracuv_vyber == 'konec':
            print("Díky za hru! Nashledanou!")
            break
        if hracuv_vyber not in vybery:
            print("Neplatný výběr, zkus to znovu.")
            continue

        # Výběr počítače
        pocitac_vyber = random.choice(vybery)
        print(f"Počítač si vybral: {pocitac_vyber}")

        # Určení výsledku
        if hracuv_vyber == pocitac_vyber:
            print("Remíza!")
        elif (hracuv_vyber == "kámen" and pocitac_vyber == "nůžky") or \
             (hracuv_vyber == "nůžky" and pocitac_vyber == "papír") or \
             (hracuv_vyber == "papír" and pocitac_vyber == "kámen"):
            print("Vyhrál jsi!")
        else:
            print("Počítač vyhrál!")

# Spuštění hry
hra_kamen_nuzky_papir()
