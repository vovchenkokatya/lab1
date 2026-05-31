def div_taylor(x, eps):
    term = 1
    s = term
    k = 1
    while abs(term) >= eps:
        term = term * (-x)
        s += term
        k += 1
    return s, k

if __name__ == '__main__':
    x = 0.5
    eps = 0.000001

    approx_val, steps = div_taylor(x, eps)

    print(approx_val)