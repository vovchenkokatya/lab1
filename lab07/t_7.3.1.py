import math

class RationalError(ZeroDivisionError):
    def __init__(self, message="Знаменник не може дорівнювати нулю"):
        super().__init__(message)

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

        if d == 0:
            raise RationalError()

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

    def __add__(self, other):
        if isinstance(other, int): other = Rational(other)
        return Rational(self._n * other.d + other.n * self._d, self._d * other.d)

    def __repr__(self):
        return f"{self._n}/{self._d}" if self._d != 1 else f"{self._n}"

class RationalList:
    def __init__(self, items=None):
        self._list = []
        if items:
            for item in items: self.append(item)

    def append(self, value):
        if isinstance(value, int): value = Rational(value)
        if not isinstance(value, Rational):
            raise TypeError("Можна додавати лише Rational або int")
        self._list.append(value)

    def __iter__(self):
        sorted_elements = sorted(
            self._list,
            key=lambda x: (-x.d, -x.n)
        )
        return iter(sorted_elements)

    def __len__(self):
        return len(self._list)

    def total_sum(self):
        if not self._list: return Rational(0)
        res = self._list[0]
        for i in range(1, len(self._list)):
            res = res + self._list[i]
        return res

def run_task(filenames):
    for fname in filenames:
        rl = RationalList()
        try:
            with open(fname, 'r') as f:
                for line in f:
                    for part in line.split():
                        try:
                            rl.append(Rational(part))
                        except (ValueError, RationalError):
                            continue

            print(f"Сума всіх чисел: {rl.total_sum()}")
            print("Елементи у порядку спадання (за ітератором):")
            for item in rl:
                print(item, end="; ")
            print("\n")
        except FileNotFoundError:
            print(f"Файл {fname} не знайдено.\n")

if __name__ == "__main__":

    run_task(['input01.txt'])