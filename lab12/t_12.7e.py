def sqrt_taylor(x, eps):
    term = x / 2   # Це перший член (після одиниці)
    s = 1 + term   # Початкова сума: 1 + x/2
    k = 2
    while abs(term) >= eps:
        term = term * (-x) * (2 * k - 3) / (2 * k)
        s += term
        k += 1
    return s, k

if __name__ == '__main__':
    x = 0.5
    eps = 0.000001

    approx_val, steps = sqrt_taylor(x, eps)

    print(approx_val)