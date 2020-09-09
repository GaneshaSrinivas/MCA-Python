from abc import *
from math import sqrt 
class Polygon(ABC):
    @abstractmethod
    def area(self,side):
        pass
class AreaSquare(Polygon):
    def area(self,side):
        area = side * side 
        return area
class AreaPentagon(Polygon):
    def area(self, side):
        area = (sqrt(5 * (5 + 2 *(sqrt(5)))) * side * side) / 4
        return area
class AreaHexagon(Polygon):
    def area(self, side):
        area= ((3 * sqrt(3) * (side * side)) / 2)
        return area
side=int(input("Enter a side "))
sq=AreaSquare()
print("Area of a Squre ", sq.area(side))
penta=AreaPentagon()
print("Area of Regular Pentagon ",penta.area(side))
hexa=AreaHexagon()
print("Area of Regular Hexagon ",hexa.area(side))
