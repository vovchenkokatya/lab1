def sum_a(n):
    total = 0
    for i in range(1, n + 1):
        total += ((-1) ** (i - 1)) * i
    return total

def sum_b(n):
    if n < 2:
        return 0

    total = 0
    for i in range(2, n + 1):
        total += 1 / ((i - 1) * i)
    return total

def sum_c(n):
    total = 0
    for i in range(2, n + 1):
        term = ((-1) ** i) * (i - 1) / i
        total += term
    return total