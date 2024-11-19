class Auto:
    
    def __init__(self, znacka, model, rok):
        self.znacka = znacka
        self.model = model
        self.rok = rok

    
    def info(self):
        return f"{self.znacka} {self.model}, vyrobeno v roce {self.rok}."


moje_auto = Auto("Volkswagen", "EOS", 2008)
print(moje_auto.info())
