import math

class Kruh:
    def __init__(self, polomer):
        self.polomer = polomer

    def obvod(self):
        return 2 * math.pi * self.polomer

    def obsah(self):
        return math.pi * (self.polomer ** 2)


kruh1 = Kruh(5)
print(f"Obvod kruhu: {kruh1.obvod():.2f}")  
print(f"Obsah kruhu: {kruh1.obsah():.2f}") 
