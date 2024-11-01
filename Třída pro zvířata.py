class Zvire:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def zvuk(self):
        return "Neznámý zvuk"

class Pes(Zvire):
    def zvuk(self):
        return "Haf haf!"

class Kocka(Zvire):
    def zvuk(self):
        return "Mňau!"


pes = Pes("Pes")
kocka = Kocka("Kočka")

print(f"{pes.jmeno} dělá: {pes.zvuk()}") 
print(f"{kocka.jmeno} dělá: {kocka.zvuk()}")
