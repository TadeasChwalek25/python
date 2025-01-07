from abc import ABC, abstractmethod

# Abstraktní třída Zivocich
class Zivocich(ABC):

    @abstractmethod
    def ozvi_se(self):
        """Každý živočich se musí umět ozvat."""
        pass

    @abstractmethod
    def pohybuj_se(self):
        """Každý živočich musí mít způsob pohybu."""
        pass

# Konkrétní třída Lev
class Lev(Zivocich):

    def ozvi_se(self):
        return "Lev řve: Roaaar!"

    def pohybuj_se(self):
        return "Lev se pohybuje běháním po souši."

# Konkrétní třída Orel
class Orel(Zivocich):

    def ozvi_se(self):
        return "Orel křičí: Kiááá!"

    def pohybuj_se(self):
        return "Orel létá vysoko na obloze."

# Konkrétní třída Ryba
class Ryba(Zivocich):

    def ozvi_se(self):
        return "Ryba dělá: ... (Ryby nevydávají zvuky)"

    def pohybuj_se(self):
        return "Ryba plave ve vodě."

# Vytvoření instancí jednotlivých živočichů
lev = Lev()
orel = Orel()
ryba = Ryba()

# Výpis výsledků
print("Lev:")
print(lev.ozvi_se())
print(lev.pohybuj_se())

print("\nOrel:")
print(orel.ozvi_se())
print(orel.pohybuj_se())

print("\nRyba:")
print(ryba.ozvi_se())
print(ryba.pohybuj_se())
