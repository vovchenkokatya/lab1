def sin_taylor(x, eps):
    a = x
    s = a
    k = 1

    while abs(a) >= eps:
        a = a * (-x**2) / ((2 * k) * (2 * k + 1))
        s += a
    return s

if __name__ == '__main__':
    x = 0.5
    eps = 0.000001

    approx_val = sin_taylor(x, eps)

    print(approx_val)
