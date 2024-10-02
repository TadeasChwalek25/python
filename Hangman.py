import random

def zobraz_slovo(slovo, hadane_pismena):
    return " ".join([pismeno if pismeno in hadane_pismena else "_" for pismeno in slovo])

def hangman():
    slova = ['programovaní', 'python', 'apple', 'mobil', 'auto']
    slovo = random.choice(slova)
    hadane_pismena = set()
    spatne_pokusy = 0
    max_spatnych_pokusu = 6

    print("Vítej ve hře Šibenice!")
    
    while spatne_pokusy < max_spatnych_pokusu:
        print("\nHádáš slovo: ", zobraz_slovo(slovo, hadane_pismena))
        print(f"Zbývající pokusy: {max_spatnych_pokusu - spatne_pokusy}")
        
        hadani = input("Hádej písmeno: ").lower()

        if len(hadani) != 1 or not hadani.isalpha():
            print("Prosím, zadej jedno písmeno.")
            continue
        
        if hadani in hadane_pismena:
            print("Toto písmeno už bylo hádáno.")
            continue
        
        hadane_pismena.add(hadani)

        if hadani in slovo:
            print(f"Písmeno '{hadani}' je ve slově!")
        else:
            print(f"Písmeno '{hadani}' není ve slově.")
            spatne_pokusy += 1
        
        if all(pismeno in hadane_pismena for pismeno in slovo):
            print(f"\nGratuluji! Uhodl jsi slovo '{slovo}'!")
            break
    else:
        print(f"\nProhrál jsi! Slovo bylo '{slovo}'.")

# Spuštění hry
hangman()
