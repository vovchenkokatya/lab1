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

    def __add__(self, other):
        if isinstance(other, int): other = Rational(other)
        return Rational(self._n * other._d + other._n * self._d, self._d * other._d)

    def __repr__(self):
        return f"{self._n}/{self._d}" if self._d != 1 else f"{self._n}"

class RationalList:
    def __init__(self, items=None):
        self._list = []
        if items:
            for item in items:
                self.append(item)

    def _validate(self, value):
        if isinstance(value, Rational):
            return value
        if isinstance(value, int):
            return Rational(value)
        raise TypeError("Елементом RationalList може бути лише екземпляр класу Rational або int")

    def append(self, value):
        self._list.append(self._validate(value))

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = self._validate(value)

    def __len__(self):
        return len(self._list)

    def __add__(self, other):
        new_list = RationalList(self._list)
        if isinstance(other, RationalList):
            for item in other._list:
                new_list.append(item)
        else:

            new_list.append(other)
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for item in other._list:
                self.append(item)
        else:
            self.append(other)
        return self

    def sum(self):

        if not self._list:
            return Rational(0)
        total = self._list[0]
        for i in range(1, len(self._list)):
            total = total + self._list[i]
        return total

def process_rational_files(filenames):
    for filename in filenames:
        r_list = RationalList()
        try:
            with open(filename, 'r') as f:
                for line in f:
                    parts = line.split()
                    for p in parts:
                        try:
                            r_list.append(Rational(p))
                        except ValueError:
                            continue

            if len(r_list) > 0:
                print(f"Кількість чисел у списку: {len(r_list)}")
                print(f"Сума послідовності: {r_list.sum()}")
            else:
                print("Файл порожній або не містить коректних чисел.")
            print()
        except FileNotFoundError:
            print(f"Помилка: Файл {filename} не знайдено.\n")

if __name__ == "__main__":

    with open('input01.txt', 'w') as f:
        f.write("1/2 3  5/4 \n 10 2/3")

    files_to_process = ['input01.txt']
    process_rational_files(files_to_process)