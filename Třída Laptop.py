class Laptop:
    def __init__(self, vyrobce, model, kapacita_baterie):
        self.vyrobce = vyrobce
        self.model = model
        self.kapacita_baterie = kapacita_baterie  

    def baterie_info(self):
        return f"{self.vyrobce} {self.model} má kapacitu baterie {self.kapacita_baterie} mAh."

laptop = Laptop("Acer", "Nitro 5", 7500)
print(laptop.baterie_info())
