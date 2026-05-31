def ln_taylor(x, eps):
    term = x
    s = term
    k = 2
    while abs(term) >= eps:
        term = term * (-x) * (k - 1) / k
        s += term
        k += 1
    return s, k

if __name__ == '__main__':
    x = 0.5
    eps = 0.000001

    approx_val, steps = ln_taylor(x, eps)

    print(approx_val)