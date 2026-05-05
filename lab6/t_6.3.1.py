"""6.3.1. Для класу RationalList , описаного під час виконання задачі 5.3.2,
реалізуйте підтримку ітераційного протоколу таким чином, щоб ітератор
перебирав усі елементи списку у порядку спадання знаменників. При рівності
знаменників, пріоритетнішим має бути число з більшим чисельником.
Виведіть на екран дані послідовність раціональних чисел для наборів вхідних
даних заданих у задачі 5.3.2. """

import math

class Rational:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                n, d = map(int, args[0].split('/'))
            elif isinstance(args[0], Rational):
                n, d = args[0]._n, args[0]._d
            else:
                n, d = args[0], 1
        elif len(args) == 2:
            n, d = args
        else:
            raise ValueError("Некоректні аргументи")

        common = math.gcd(n, d)
        self._n = n // common
        self._d = d // common
        if self._d < 0:
            self._n = -self._n
            self._d = -self._d

    @property
    def n(self): return self._n
    @property
    def d(self): return self._d

    def __repr__(self):
        return f"{self._n}/{self._d}" if self._d != 1 else f"{self._n}"

class RationalList:
    def __init__(self, items=None):
        self._list = []
        if items:
            for item in items:
                self.append(item)

    def append(self, value):
        if isinstance(value, int):
            value = Rational(value)
        if not isinstance(value, Rational):
            raise TypeError("Тільки Rational або int")
        self._list.append(value)

    def __iter__(self):
        sorted_elements = sorted(
            self._list,
            key=lambda x: (-x.d, -x.n)
        )
        return iter(sorted_elements)

    def __len__(self):
        return len(self._list)

def process_and_print_sorted(filenames):
    for filename in filenames:
        r_list = RationalList()
        try:
            with open(filename, 'r') as f:
                for line in f:
                    for p in line.split():
                        try:
                            r_list.append(Rational(p))
                        except (ValueError, ZeroDivisionError):
                            continue

            for rational in r_list:
                print(rational)
            print()
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено.\n")

if __name__ == "__main__":

    process_and_print_sorted(['input01.txt'])

