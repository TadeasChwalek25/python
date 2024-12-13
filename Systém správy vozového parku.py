from abc import ABC, abstractmethod

# Abstraktní třída pro všechna vozidla
class Vozidlo(ABC):
    def __init__(self, znacka, model, rok):
        self.znacka = znacka
        self.model = model
        self.rok = rok

    @abstractmethod
    def informace(self):
        pass

# Třída pro osobní vozidla
class OsobniAuto(Vozidlo):
    def __init__(self, znacka, model, rok, pocet_sedadel):
        super().__init__(znacka, model, rok)
        self.pocet_sedadel = pocet_sedadel

    def informace(self):
        return f"Osobní auto: {self.znacka} {self.model}, rok: {self.rok}, sedadel: {self.pocet_sedadel}"

# Třída pro nákladní vozidla
class NakladniAuto(Vozidlo):
    def __init__(self, znacka, model, rok, kapacita):
        super().__init__(znacka, model, rok)
        self.kapacita = kapacita  # Kapacita v tunách

    def informace(self):
        return f"Nákladní auto: {self.znacka} {self.model}, rok: {self.rok}, kapacita: {self.kapacita} tun"

# Třída pro správu vozového parku
class VozovyPark:
    def __init__(self):
        self.vozidla = []

    def pridej_vozidlo(self, vozidlo):
        if isinstance(vozidlo, Vozidlo):
            self.vozidla.append(vozidlo)
        else:
            raise ValueError("Přidávaný objekt není typ Vozidlo")

    def zobraz_vsechna_vozidla(self):
        for vozidlo in self.vozidla:
            print(vozidlo.informace())

    def celkova_kapacita(self):
        kapacita = sum(vozidlo.kapacita for vozidlo in self.vozidla if isinstance(vozidlo, NakladniAuto))
        return f"Celková kapacita všech nákladních vozidel: {kapacita} tun"

# Vytvoření vozového parku
park = VozovyPark()

# Přidání různých vozidel
park.pridej_vozidlo(OsobniAuto("Volkswagen", "EOS", 2008, 4))
park.pridej_vozidlo(NakladniAuto("Scania", "S", 2024, 18))
park.pridej_vozidlo(NakladniAuto("Mercedes", "Actros", 2023, 20))

# Zobrazení všech vozidel
print("Informace o všech vozidlech v parku:")
park.zobraz_vsechna_vozidla()

# Zobrazení celkové kapacity nákladních vozidel
print(park.celkova_kapacita())
