import random
import time

def uvod():
    print("=" * 40)
    print("🎲 VÍTEJ VE HŘE: HÁDEJ ČÍSLO 🎲")
    print("=" * 40)
    print("Zkus uhodnout číslo, které si myslím!")
    print("Máš omezený počet pokusů – buď opatrný 😉")
    print()

def hraj():
    tajne_cislo = random.randint(1, 100)
    pokusy = 0
    max_pokusy = 7

    while pokusy < max_pokusy:
        try:
            tip = int(input(f"({pokusy+1}/{max_pokusy}) Tvůj tip: "))
        except ValueError:
            print("❌ To není číslo! Zkus to znovu.")
            continue

        pokusy += 1

        if tip == tajne_cislo:
            print(f"✅ Správně! Uhádnul jsi číslo {tajne_cislo} za {pokusy} pokusů!")
            break
        elif tip < tajne_cislo:
            print("🔼 Moje číslo je větší.")
        else:
            print("🔽 Moje číslo je menší.")

        if pokusy == max_pokusy:
            print(f"😢 Došly ti pokusy! Hledané číslo bylo {tajne_cislo}.")

def znovu():
    while True:
        odpoved = input("\nChceš hrát znovu? (a/n): ").lower()
        if odpoved == "a":
            print("\nNačítám novou hru...")
            time.sleep(1)
            return True
        elif odpoved == "n":
            print("Díky za hraní! 👋")
            return False
        else:
            print("Prosím napiš 'a' nebo 'n'.")

if __name__ == "__main__":
    uvod()
    while True:
        hraj()
        if not znovu():
            break
