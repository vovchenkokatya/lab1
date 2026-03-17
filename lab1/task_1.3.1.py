import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.name = "Трикутник"

    def perim(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 0
        return self.a + self.b + self.c

    def area(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 0
        p = self.perim() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Rectangle:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
        self.name = "Прямокутник"

    def perim(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)
        self.name = "Трапеція"

    def perim(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        if self.a == self.b:
            return self.a * self.b
        other = abs(self.a - self.b)
        p = (other + self.c + self.d) / 2
        perev = p * (p - other) * (p - self.c) * (p - self.d)
        if perev < 0:
            return 0
        h = (2 / other) * math.sqrt(perev)
        return ((self.a + self.b) / 2) * h


class Parallelogram:
    def __init__(self, a, b, h):
        self.a = float(a)
        self.b = float(b)
        self.h = float(h)
        self.name = "Паралелограм"

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.h


class Circle:
    def __init__(self, r):
        self.r = float(r)
        self.name = "Круг"

    def get_perimeter(self):
        return 2 * math.pi * self.r

    def get_area(self):
        return math.pi * (self.r ** 2)


import os

def analyze(filename):
    figures_list = []

    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.split()
                if not parts:
                    continue

                try:
                    params = [float(x) for x in parts]
                except ValueError:
                    continue

                n = len(params)

                if n == 1:
                    figures_list.append(Circle(*params))
                elif n == 2:
                    figures_list.append(Rectangle(*params))
                elif n == 3:
                    figures_list.append(Triangle(*params))
                elif n == 4:
                    figures_list.append(Trapeze(*params))
                elif n == 5:
                    pass

    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
        return

    if not figures_list:
        print(f"У файлі {filename} не знайдено коректних даних для створення фігур.")
        return

    max_area_fig = max(figures_list, key=lambda f: f.area())
    max_perim_fig = max(figures_list, key=lambda f: f.perim())

    print(f"Результати для {filename}:")
    print(f"Найбільша площа: {max_area_fig.name} (Значення: {max_area_fig.area():.2f})")
    print(f"Найбільший периметр: {max_perim_fig.name} (Значення: {max_perim_fig.perim():.2f})")

files_to_process = ['input01.txt', 'input02.txt', 'input03.txt']

for file_name in files_to_process:
    analyze(file_name)