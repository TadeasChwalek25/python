class Tovarna:
    def __init__(self):
        # Seznam dostupných dárků, které může továrna vyrobit
        self.dostupne_darky = ["autíčko", "panenka", "fotbalový míč", "mobil", "tablet", "sluchátka"]
        self.vyrobene_darky = []  # Seznam pro uchování vyrobených dárků

    def vyrobDarek(self, typ_darku):
        if typ_darku in self.dostupne_darky:
            self.vyrobene_darky.append(typ_darku)
            print(f"Dárek '{typ_darku}' byl úspěšně vyroben!")
        else:
            print(f"Továrna nemůže vyrobit dárek '{typ_darku}'. Zvolte jiný.")

# Vytvoření instance třídy Tovarna
jezisekova_tovarna = Tovarna()

# Výroba dárků
jezisekova_tovarna.vyrobDarek("autíčko")
jezisekova_tovarna.vyrobDarek("tablet")
jezisekova_tovarna.vyrobDarek("sluchátka")
jezisekova_tovarna.vyrobDarek("robot")  # Tento dárek není dostupný

# Výpis vyrobených dárků
print("Vyrobené dárky:", jezisekova_tovarna.vyrobene_darky)
