class Share:
    def render(self):
        print("Initializing to render some share")

class Square(Share):
    def render(self):
        super().render()
        print("Rendering a square...")

class Triangle(Share):
    def render(self):
        super().render()
        print("Rendering a triangle...")

class Circle(Share):
    def render(self):
        super().render()
        print("Rendering a circle...")

class Pentagon(Share):
    def render(self):
        super().render()
        print("Rendering a pentagon...")

class Factory:
    __article = {
        "Square": Square,
        "Triangle": Triangle,
        "Circle": Circle,
        "Pentagon": Pentagon
    }

    @staticmethod
    def create(representative):
        return Factory.__article[representative]()

shapes = ["Square", "Triangle", "Circle", "Pentagon"]
for shape in shapes:
    my_shape = Factory.create(shape)
    my_shape.render()
