from abc import ABC, abstractmethod

# Abstraktní třída pro IT zařízení
class Zarizeni(ABC):
    def __init__(self, vyrobce, model, rok, uloziste):
        self.vyrobce = vyrobce
        self.model = model
        self.rok = rok
        self.uloziste = uloziste

    @abstractmethod
    def informace(self):
        pass

# Třída pro telefony
class Telefon(Zarizeni):
    def __init__(self, vyrobce, model, rok, uloziste, dual_sim, kapacita_baterie):
        super().__init__(vyrobce, model, rok, uloziste)
        self.dual_sim = dual_sim
        self.kapacita_baterie = kapacita_baterie

    def informace(self):
        sim_info = "Ano" if self.dual_sim else "Ne"
        return (f"Telefon: {self.vyrobce} {self.model}, rok: {self.rok}, "
                f"úložiště: {self.uloziste} GB, Dual SIM: {sim_info}, "
                f"kapacita baterie: {self.kapacita_baterie} mAh")

# Třída pro tablety
class Tablet(Zarizeni):
    def __init__(self, vyrobce, model, rok, uloziste, stylus, velikost_displeje):
        super().__init__(vyrobce, model, rok, uloziste)
        self.stylus = stylus
        self.velikost_displeje = velikost_displeje

    def informace(self):
        stylus_info = "Podporován" if self.stylus else "Nepodporován"
        return (f"Tablet: {self.vyrobce} {self.model}, rok: {self.rok}, "
                f"úložiště: {self.uloziste} GB, Stylus: {stylus_info}, "
                f"velikost displeje: {self.velikost_displeje}\"")

# Třída pro správu IT zařízení
class SpravaZarizeni:
    def __init__(self):
        self.zarizeni_list = []

    def pridej_zarizeni(self, zarizeni):
        if isinstance(zarizeni, Zarizeni):
            self.zarizeni_list.append(zarizeni)
        else:
            raise ValueError("Přidávaný objekt není typu Zarizeni")

    def zobraz_vsechna_zarizeni(self):
        for zarizeni in self.zarizeni_list:
            print(zarizeni.informace())

    def celkova_pamet(self):
        pamet = sum(zarizeni.uloziste for zarizeni in self.zarizeni_list)
        return f"Celková paměť všech zařízení: {pamet} GB"

# Vytvoření správy zařízení
sprava = SpravaZarizeni()

# Přidání různých zařízení
sprava.pridej_zarizeni(Telefon("Samsung", "Galaxy S21 Ultra 5G", 2021, 256, True, 5000))
sprava.pridej_zarizeni(Telefon("Apple", "iPhone 13 Pro", 2021, 256, False, 3095))
sprava.pridej_zarizeni(Tablet("Apple", "iPad Pro", 2022, 512, True, 12.9))
sprava.pridej_zarizeni(Tablet("Samsung", "Galaxy Tab S8", 2022, 256, True, 11.0))

# Zobrazení všech zařízení
print("Informace o všech zařízeních:")
sprava.zobraz_vsechna_zarizeni()

# Zobrazení celkové paměti
print(sprava.celkova_pamet())
