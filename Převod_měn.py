def prevod_meny():

    kurz_eur = 25.3   # 1 EUR = 25.3 Kč
    kurz_usd = 23.7   # 1 USD = 23.7 Kč
    kurz_gbp = 29.4   # 1 GBP = 29.4 Kč

    while True:
        print("=" * 40)
        print("💰 PŘEVOD MĚN – z českých korun (CZK)")
        print("=" * 40)

        try:
            castka = float(input("Zadej částku v Kč: "))
        except ValueError:
            print("❌ Neplatný vstup – zadej číslo!")
            continue

        print("\nZvol měnu pro převod:")
        print("1  EUR")
        print("2️  USD")
        print("3️  GBP")
        volba = input("Tvoje volba (1/2/3): ")

        if volba == "1":
            vysledek = round(castka / kurz_eur, 2)
            mena = "EUR"
        elif volba == "2":
            vysledek = round(castka / kurz_usd, 2)
            mena = "USD"
        elif volba == "3":
            vysledek = round(castka / kurz_gbp, 2)
            mena = "GBP"
        else:
            print("❌ Neplatná volba, zkus to znovu.")
            continue

        print(f"\n💱 {castka:.2f} Kč = {vysledek:.2f} {mena}")

        # dotaz na pokračování
        pokracovat = input("\nChceš provést další převod? (a/n): ").lower()
        if pokracovat != "a":
            print("\nDíky za použití převodníku! 👋")
            break

# Spuštění programu
if __name__ == "__main__":
    prevod_meny()
