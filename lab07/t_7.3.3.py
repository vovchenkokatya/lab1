import math

class RationalError(ZeroDivisionError):
    def __init__(self, message="Знаменник не може дорівнювати нулю"):
        super().__init__(message)

class RationalValueError(ValueError):
    def __init__(self, message="Некоректний тип даних"):
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
            raise RationalValueError(f"Неможливо додати {type(value).__name__} до RationalList. Очікується Rational або int.")

        self._list.append(value)

    def __setitem__(self, index, value):
        if isinstance(value, int):
            value = Rational(value)
        if not isinstance(value, Rational):
            raise RationalValueError("Некоректний тип при зміні елемента списку")
        self._list[index] = value

    def __iter__(self):
        sorted_elements = sorted(self._list, key=lambda x: (-x.d, -x.n))
        return iter(sorted_elements)

    def __len__(self):
        return len(self._list)

if __name__ == "__main__":
    rl = RationalList()
    rl.append(Rational(1, 2))
    rl.append(5)

    print("Список після коректного додавання:", [x for x in rl])

    try:
        print("\nСпроба додати рядок 'hello'...")
        rl.append("hello")
    except RationalValueError as e:
        print(f"Спіймано виключення 7.3.3: {e}")