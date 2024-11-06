class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def predstaveni(self):
        return f"Ahoj, jmenuji se {self.jmeno} a je mi {self.vek} let."

osoba1 = Osoba("Tadeáš", 16)
osoba2 = Osoba("Anna", 15)

print(osoba1.predstaveni())
print(osoba2.predstaveni()) 
