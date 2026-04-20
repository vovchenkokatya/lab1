import math
from base import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimention(self):
        return 2
    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = (self.a + self.b + self.c) / 2
        val = p * (p - self.a) * (p - self.b) * (p - self.c)
        return math.sqrt(val) if val > 0 else 0

    def volume(self): return self.square()

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b
    def dimention(self):
        return 2
    def perimetr(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.b
    def volume(self):
        return self.square()

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d
    def dimention(self):
        return 2
    def perimetr(self):
        return self.a + self.b + self.c + self.d
    def square(self):
        try:
            diff = abs(self.a - self.b)
            if diff == 0:
                return 0
            val = (diff**2 + self.c**2 - self.d**2) / (2 * diff)
            h_sq = self.c**2 - val**2
            return ((self.a + self.b) / 2) * math.sqrt(h_sq) if h_sq > 0 else 0
        except:
            return 0
    def volume(self): return self.square()

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h_val = a, b, h
    def dimention(self):
        return 2
    def perimetr(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.h_val
    def volume(self):
        return self.square()

class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def dimention(self):
        return 2
    def perimetr(self):
        return 2 * math.pi * self.r
    def square(self):
        return math.pi * (self.r ** 2)
    def volume(self):
        return self.square()

