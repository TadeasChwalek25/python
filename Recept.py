class Recept:
    def __init__(self, nazev, pocet_porci):
        self.nazev = nazev
        self.pocet_porci = pocet_porci
        self.ingredience = []

    def pridat_ingredienci(self, ingredience):
        self.ingredience.append(ingredience)
        return f"Ingredience '{ingredience}' byla přidána do receptu '{self.nazev}'."

    def zobraz_recept(self):
        return f"Recept: {self.nazev}\nPočet porcí: {self.pocet_porci}\nIngredience: {', '.join(self.ingredience)}"

# Použití třídy
recept = Recept("Palačinky", 4)
print(recept.pridat_ingredienci("Mléko"))
print(recept.pridat_ingredienci("Mouka"))
print(recept.pridat_ingredienci("Vejce"))
print(recept.zobraz_recept())
