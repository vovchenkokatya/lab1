import math

def E(x, eps):
    a = 1.0
    s = a
    k = 1

    while abs(a) >= eps:
        a = a * (-x) * (2 * k - 1) / (2 * k)
        s += a
    return s

if __name__ == '__main__':
    x = 0.5
    eps = 0.000001

    approx_val = E(x, eps)
    exact_val = 1 / math.sqrt(1 + x)

    print(approx_val)
    print(exact_val)
