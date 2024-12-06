class ChristmasTree:
    def __init__(self, height, color):
        self.height = height  # výška stromku
        self.color = color  # barva stromku
        self.decorations = []  # seznam ozdob
    
    def add_decoration(self, decoration):
        """Přidá ozdobu na stromek."""
        self.decorations.append(decoration)
    
    def show_tree(self):
        """Vypíše stromek a jeho ozdoby."""
        print(f"Vánoční stromek: {self.height} cm, barva: {self.color}")
        print("Ozdoby:")
        for decoration in self.decorations:
            print(f"- {decoration}")
    

class Decoration:
    def __init__(self, name, color):
        self.name = name  # název ozdoby
        self.color = color  # barva ozdoby
    
    def __str__(self):
        return f"{self.color} {self.name}"


class ChristmasBall(Decoration):
    def __init__(self, color, size):
        super().__init__("vánoční koule", color)
        self.size = size  # velikost koule
    
    def __str__(self):
        return f"{self.color} vánoční koule ({self.size} cm)"


class ChristmasChain(Decoration):
    def __init__(self, color, length):
        super().__init__("vánoční řetěz", color)
        self.length = length  # délka řetězu
    
    def __str__(self):
        return f"{self.color} vánoční řetěz ({self.length} m)"


class ChristmasCandy(Decoration):
    def __init__(self, flavor):
        super().__init__("vánoční kolekce", "barevná")
        self.flavor = flavor  # chuť cukroví
    
    def __str__(self):
        return f"barevná vánoční kolekce (chuť: {self.flavor})"


# Vytvoření vánočního stromku
tree = ChristmasTree(height=200, color="zelený")

# Přidání ozdob
tree.add_decoration(ChristmasBall(color="červená", size=10))
tree.add_decoration(ChristmasBall(color="zlatá", size=8))
tree.add_decoration(ChristmasChain(color="stříbrný", length=5))
tree.add_decoration(ChristmasCandy(flavor="čokoláda"))

# Zobrazení stromku a jeho ozdob
tree.show_tree()
