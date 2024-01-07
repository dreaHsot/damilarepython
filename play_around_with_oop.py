class Circles:
    pi = 22/7
    def __init__(self, name, radius) -> None:
        self.name = name
        self.radius = radius
        self.area = self.pi * (radius ** 2)
        self.perimeter = self.pi * radius * 2
    def showarea(self):
        print(f"The area of the {self.name} is {self.area}")
    def showperimeter(self):
        print(f"The circumference of the {self.name} is {self.perimeter}")

# c1 = Circles('sphere', 7)
# c1.showarea()
# c2 = Circles('small circle', 3.5)
# c2.showarea()
# c2.showperimeter()
# c1.showperimeter()
        
class Rectangle(Circles):
    def __init__(self, name, radius) -> None:
        super().__init__(name, radius)
        