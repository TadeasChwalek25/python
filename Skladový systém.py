from datetime import datetime

# Třída Produkt
class Produkt:
    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

    def __str__(self):
        return f"{self.nazev} - {self.cena} Kč"

# Specializovaná třída Potravina dědící od Produkt
class Potravina(Produkt):
    def __init__(self, nazev, cena, datum_spotreby):
        super().__init__(nazev, cena)
        self.datum_spotreby = datetime.strptime(datum_spotreby, "%Y-%m-%d")

    def je_po_datum_spotreby(self):
        """Kontrola, zda je potravina po datu spotřeby."""
        return datetime.now() > self.datum_spotreby

    def __str__(self):
        stav = "po datu spotřeby" if self.je_po_datum_spotreby() else "v pořádku"
        return f"{self.nazev} - {self.cena} Kč (Spotřeba do: {self.datum_spotreby.date()}, {stav})"

# Třída Sklad
class Sklad:
    def __init__(self):
        self.produkty = []

    def pridej_produkt(self, produkt):
        """Přidá produkt do skladu."""
        self.produkty.append(produkt)
        print(f"Produkt '{produkt.nazev}' byl přidán do skladu.")

    def zobraz_produkty(self):
        """Vypíše všechny produkty ve skladu."""
        if not self.produkty:
            print("Sklad je prázdný.")
        else:
            print("Seznam produktů ve skladu:")
            for produkt in self.produkty:
                print(f" - {produkt}")

# Testovací část
# Vytvoření skladu
sklad = Sklad()

# Vytvoření produktů
jablko = Potravina("Jablko", 10, "2024-06-01")
chleba = Potravina("Chleba", 30, "2024-05-01")
televize = Produkt("Televize Samsung", 15000)

# Přidání produktů do skladu
sklad.pridej_produkt(jablko)
sklad.pridej_produkt(chleba)
sklad.pridej_produkt(televize)

# Zobrazení všech produktů
sklad.zobraz_produkty()
