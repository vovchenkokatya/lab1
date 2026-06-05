import math

def generate(x, eps):
    a = 2 * x
    s = 2 * x
    k = 2

    while abs(a) > eps:
        yield s
        a *= (x**2 * (2 * k - 3)) / (2 * k - 1)
        s += a
        k += 1

if __name__ == '__main__':
    x_val = 0.5
    eps_val = 0.001

    for item in generate(x_val, eps_val):
        print(item)

    print()
    print(math.log((1 + x_val) / (1 - x_val)))