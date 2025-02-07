class Pocitadlo:
    def __init__(self):
        self.pocet = 0

    def zvysit(self):
        self.pocet += 1
        print(f"Počet zvýšen na: {self.pocet}")

    def snizit(self):
        if self.pocet > 0:
            self.pocet -= 1
            print(f"Počet snížen na: {self.pocet}")
        else:
            print("Počet je již na nule a nelze jej snížit.")

    def resetovat(self):
        self.pocet = 0
        print("Počet byl resetován na nulu.")

if __name__ == "__main__":
    pocitadlo = Pocitadlo()
    print("Jednoduché Počítadlo")
    print("Příkazy: 'zvysit', 'snizit', 'resetovat', 'konec'")

    while True:
        prikaz = input("Zadej příkaz: ").lower()
        if prikaz == "zvysit":
            pocitadlo.zvysit()
        elif prikaz == "snizit":
            pocitadlo.snizit()
        elif prikaz == "resetovat":
            pocitadlo.resetovat()
        elif prikaz == "konec":
            print("Bye-bye!")
            break
        else:
            print("Neplatný příkaz. Zkuste to znovu.")
