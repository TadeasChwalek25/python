from abc import ABC, abstractmethod

# Abstraktní třída Vozidlo
class Vozidlo(ABC):
    def __init__(self, znacka, model):
        self.znacka = znacka
        self.model = model

    @abstractmethod
    def start(self):
        """Abstraktní metoda pro start vozidla."""
        pass

# Třída Auto, která dědí z Vozidlo
class Auto(Vozidlo):
    def __init__(self, znacka, model, pocet_dveri):
        super().__init__(znacka, model)
        self.pocet_dveri = pocet_dveri

    def start(self):
        return f"Auto {self.znacka} {self.model} startuje se {self.pocet_dveri} dveřmi."

# Třída Motorka, která dědí z Vozidlo
class Motorka(Vozidlo):
    def __init__(self, znacka, model, typ_motorky):
        super().__init__(znacka, model)
        self.typ_motorky = typ_motorky

    def start(self):
        return f"Motorka {self.znacka} {self.model} typu {self.typ_motorky} startuje."

# Vytvoření instancí třídy Auto
auto1 = Auto("Škoda", "Octavia", 5)
auto2 = Auto("BMW", "X5", 3)

# Vytvoření instancí třídy Motorka
motorka1 = Motorka("Yamaha", "MT-07", "naháč")
motorka2 = Motorka("Honda", "CBR600RR", "sportovní")

# Výpis výsledků
print(auto1.start())
print(auto2.start())

print(motorka1.start())
print(motorka2.start())
