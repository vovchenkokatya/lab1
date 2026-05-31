def a(x, eps):
    if x == 0:
        return 0.0

    x_prev = x / 3
    while True:
        x_n = (1 / 3) * (2 * x_prev + x / (x_prev**2))
        if abs(x_n - x_prev) < eps:
            return x_n
        x_prev = x_n

def b(x, eps):
    if x == 0:
        return 0.0

    x_n = x / 3
    while abs(x_n**3 - x) >= eps:
        x_n = (1 / 3) * (2 * x_n + x / (x_n**2))

    return x_n

if __name__ == '__main__':
    x = 27
    eps = 0.000001

    print(a(x, eps))
    print(b(x, eps))