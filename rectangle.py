from points import *

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return "[{}, {}]".format(self.pt1, self.pt2)
    
    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return (self.pt1, self.pt2) == (other.pt1, other.pt2)
    
    def __ne__(self, other):        # obsługa rect1 != rect2
        return (self.pt1, self.pt2) != (other.pt1, other.pt2)

    def center(self):          # zwraca środek prostokąta
        return Point((self.pt2.x + self.pt1.x) / 2, (self.pt2.y + self.pt1.y) / 2)  
    
    def area(self):            # pole powierzchni
        return abs((self.pt1.x - self.pt2.x) * (self.pt2.y - self.pt1.y))
    
    def move(self, x, y):      # przesunięcie o (x, y)
        m = Point(x, y)
        self.pt1 += m
        self.pt2 += m
        return self