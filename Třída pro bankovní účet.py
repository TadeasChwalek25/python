class BankovniUcet:
    def __init__(self, jmeno, zustatek=0):
        self.jmeno = jmeno
        self.zustatek = zustatek

    def vklad(self, castka):
        self.zustatek += castka
        return f"Na účet bylo vloženo {castka} Kč."

    def vyber(self, castka):
        if self.zustatek >= castka:
            self.zustatek -= castka
            return f"Z účtu bylo vybráno {castka} Kč."
        else:
            return "Nedostatečný zůstatek!"

    def zobraz_zustatek(self):
        return f"Aktuální zůstatek: {self.zustatek} Kč."

# Použití
ucet = BankovniUcet("Tomáš", 1000)
print(ucet.vklad(500))  
print(ucet.vyber(300))  
print(ucet.zobraz_zustatek())  
