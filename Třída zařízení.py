class Zarizeni:
    def __init__(self, vyrobce, model):
        self.vyrobce = vyrobce
        self.model = model

class Tablet(Zarizeni):
    def __init__(self, vyrobce, model, stylus):
        super().__init__(vyrobce, model)
        self.stylus = stylus

    def stylus_info(self):
        return f"{self.vyrobce} {self.model} podporuje stylus: {'Ano' if self.stylus else 'Ne'}."

# Vytvoření objektu
tablet = Tablet("Apple", "iPad Pro", True)
print(tablet.stylus_info())
