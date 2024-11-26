class SmartWatch:
    def __init__(self, vyrobce, model):
        self.vyrobce = vyrobce
        self.model = model
        self.kroky = 0

    def pridat_kroky(self, kroky):
        self.kroky += kroky
        return f"Aktuální počet kroků: {self.kroky}"

# Vytvoření objektu a přidání kroků
hodinky = SmartWatch("Garmin", "Forerunner")
print(hodinky.pridat_kroky(2500))
print(hodinky.pridat_kroky(5000))
