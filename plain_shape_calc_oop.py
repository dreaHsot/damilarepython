class Circle:
    pi = 22 / 7
    def __init__(self, r) -> None:
        self.r = r
    def calc_area(self):
        area = self.pi * self.r * self.r
        return area
Circle_1 = Circle(7)
print(Circle_1.r)
print(Circle_1.pi)
print(Circle_1.calc_area())

class Rectangle:
    def __init__(self, length, breadth) -> None:
        self.l = length
        self.b = breadth
    def calc_area(self):
        area = self.l * self.b
        return area
    
R_1 = Rectangle(10, 5)
print(R_1.calc_area())