# geometry.py
class Shape:
    def __init__(self, name):
        self.name = name

    def surface_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def surface_area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("rectangle")
        self.length = length
        self.width = width

    def surface_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def surface_area(self):
        return 3.14 * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("triangle")
        self.base = base
        self.height = height

    def surface_area(self):
        return 0.5 * self.base * self.height
