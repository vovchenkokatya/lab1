import math

def prod_a(n):
    if n < 2:
        return 1
    p = 1
    for i in range(2, n + 1):
        p *= (1 - 1 / (i ** 2))
    return p

def prod_b(n):
    p = 1
    for i in range(1, n + 1):
        p *= (2 + 1 / math.factorial(i))
    return p

def prod_c(n):
    p = 1
    for i in range(1, n + 1):
        p *= (i + 1) / (i + 2)
    return p