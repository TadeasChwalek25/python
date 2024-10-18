class Automobil:
    def __init__(self, znacka, palivo):
        self.znacka = znacka
        self.palivo = palivo
        self.nastartovano = False

    def nastartovat(self):
        if self.nastartovano:
            return f"{self.znacka} už je nastartovaný."
        self.nastartovano = True
        return f"{self.znacka} je nastartovaný."

    def zastavit(self):
        if not self.nastartovano:
            return f"{self.znacka} už je zastavený."
        self.nastartovano = False
        return f"{self.znacka} je zastavený."

    def tankovat(self, mnozstvi):
        self.palivo += mnozstvi
        return f"Natankováno {mnozstvi} litrů. Aktuální palivo: {self.palivo} litrů."

auto = Automobil("BMW", 10)
print(auto.nastartovat())  
print(auto.tankovat(20)) 
print(auto.zastavit())
