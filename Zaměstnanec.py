class Zamestnanec:
    def __init__(self, jmeno, pozice, plat):
        self.jmeno = jmeno
        self.pozice = pozice
        self.plat = plat

    def zvyseni_platu(self, castka):
        self.plat += castka
        return f"Plat zaměstnance {self.jmeno} byl zvýšen o {castka} Kč."

    def zobraz_info(self):
        return f"Zaměstnanec: {self.jmeno}, Pozice: {self.pozice}, Plat: {self.plat} Kč měsíčně."


zamestnanec1 = Zamestnanec("Petr", "Manažer", 120000)
print(zamestnanec1.zobraz_info())  
print(zamestnanec1.zvyseni_platu(25000))
