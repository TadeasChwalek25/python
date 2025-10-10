def bmi(vyska, hmotnost):
    
    # Spočítá BMI pomocí vzorce `hmotnost / (vyska / 100) ** 2`. Vrací hodnotu BMI.
    
    return hmotnost / (vyska / 100) ** 2

def kategorie_bmi(bmi_hodnota):
   
   # Určuje kategorii na základě hodnoty BMI. Vrací kategorii.
   
    if bmi_hodnota < 18.5:
        return "podváha"
    elif bmi_hodnota < 25:
        return "normální váha"
    elif bmi_hodnota < 30:
        return "nadváha"
    else:
        return "obezita"

# hlavní program
vyska = float(input("Zadejte svou výšku v metrech: "))
hmotnost = float(input("Zadejte svou hmotnost v kilogramech: "))

bmi_hodnota = bmi(vyska, hmotnost)
kategorie = kategorie_bmi(bmi_hodnota)

print(f"Index tělesné hmotnosti: {bmi_hodnota:.2f}")
print(f"Kategorie: {kategorie}")
