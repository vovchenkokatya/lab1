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
            raise ValueError("Некоректні аргументи для конструктора")

        if d == 0:
            raise ZeroDivisionError("Знаменник не може бути нулем")

        common = math.gcd(n, d)
        self._n = n // common
        self._d = d // common

        if self._d < 0:
            self._n = -self._n
            self._d = -self._d

    def __getitem__(self, key):
        if key == 'n': return self._n
        if key == 'd': return self._d
        raise KeyError("Використовуйте 'n' або 'd'")

    def __setitem__(self, key, value):
        if key == 'n': self._n = value
        elif key == 'd':
            if value == 0: raise ZeroDivisionError()
            self._d = value
        else: raise KeyError("Використовуйте 'n' або 'd'")
        # Перерахунок після зміни
        new_r = Rational(self._n, self._d)
        self._n, self._d = new_r._n, new_r._d

    # Перетворення на десятковий дріб через виклик ()
    def __call__(self):
        return self._n / self._d

    # Арифметичні операції
    def __add__(self, other):
        other = self._to_rational(other)
        return Rational(self._n * other._d + other._n * self._d, self._d * other._d)

    def __sub__(self, other):
        other = self._to_rational(other)
        return Rational(self._n * other._d - other._n * self._d, self._d * other._d)

    def __mul__(self, other):
        other = self._to_rational(other)
        return Rational(self._n * other._n, self._d * other._d)

    def __truediv__(self, other):
        other = self._to_rational(other)
        return Rational(self._n * other._d, self._d * other._n)

    def _to_rational(self, other):
        if isinstance(other, int):
            return Rational(other, 1)
        if isinstance(other, Rational):
            return other
        raise TypeError("Операція можлива лише з цілим числом або класом Rational")

    def __repr__(self):
        return f"{self._n}/{self._d}" if self._d != 1 else f"{self._n}"

def solve_expressions(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line: continue

                tokens = line.split()
                processed_tokens = []
                for t in tokens:
                    if t.isdigit():
                        processed_tokens.append(f"Rational({t})")
                    elif '/' in t:
                        processed_tokens.append(f"Rational('{t}')")
                    else:
                        processed_tokens.append(t)

                expr = " ".join(processed_tokens)
                result = eval(expr)
                print(f"Вираз: {line}")
                print(f"Результат (дріб): {result}")
                print(f"Результат (десятковий): {result()}\n")
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")

if __name__ == "__main__":

    solve_expressions('input01.txt')