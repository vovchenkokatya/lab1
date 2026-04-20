import math
from base import Figure
from figures_2d import Triangle, Rectangle, Circle

class Ball(Figure):

    def __init__(self, r):
        self.r = r

    def dimention(self):
        return 3
    def volume(self):
        return (4/3) * math.pi * (self.r ** 3)
    def square(self):
        return None
    def perimetr(self):
        return None

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimention(self):
        return 3
    def perimetr(self):
        return None
    def height(self):
        return self.h
    def squareBase(self):
        return super().square()
    def volume(self):
        return (1/3) * self.squareBase() * self.h

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimention(self):
        return 3
    def perimetr(self):
        return None
    def height(self):
        return self.h
    def squareBase(self):
        return super().square()
    def volume(self):
        return (1/3) * self.squareBase() * self.h

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimention(self):
        return 3
    def perimetr(self):
        return None
    def height(self):
        return self.c
    def squareBase(self):
        return super().square()
    def volume(self):
        return self.squareBase() * self.c

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h

    def dimention(self):
        return 3
    def perimetr(self):
        return None
    def height(self):
        return self.h
    def squareBase(self):
        return super().square()
    def volume(self):
        return (1/3) * math.pi * (self.r ** 2) * self.h

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimention(self):
        return 3
    def perimetr(self):
        return None
    def height(self):
        return self.h
    def squareBase(self):
        return super().square()
    def volume(self):
        return self.squareBase() * self.h

