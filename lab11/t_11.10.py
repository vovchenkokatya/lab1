def continued_fraction(n):
    result = 0
    for k in range(n, 0, -1):
        denominator = 4 * k + 2
        result = 1 / (denominator + result)

    return 2 + result