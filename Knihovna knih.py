class Knihovna:
    def __init__(self):
        self.knihy = []

    def pridat_knihu(self, kniha):
        self.knihy.append(kniha)
        return f"Kniha '{kniha}' byla přidána."

    def odebrat_knihu(self, kniha):
        if kniha in self.knihy:
            self.knihy.remove(kniha)
            return f"Kniha '{kniha}' byla odebrána."
        return f"Kniha '{kniha}' nebyla nalezena."

    def zobrazit_knihy(self):
        if self.knihy:
            return "Knihy v knihovně: " + ", ".join(self.knihy)
        return "Knihovna je prázdná."


moje_knihovna = Knihovna()
print(moje_knihovna.pridat_knihu("1984"))  
print(moje_knihovna.pridat_knihu("Hobit"))  
print(moje_knihovna.zobrazit_knihy())  
print(moje_knihovna.odebrat_knihu("1984"))
