import math

def seq_a(x, k):
    numerator = x ** (2 * k + 1)
    denominator = math.factorial(2 * k + 1)
    return numerator / denominator

def seq_b(x, k):
    if k < 1:
        return "Помилка: k має бути >= 1"

    return ((-1) ** k * x ** k) / k

def seq_c(x, k):
    numerator = (-1) ** k * x ** k
    denominator = math.factorial(k**2 + k)
    return numerator / denominator

def seq_d(x, k):
    return (k + 1) * (x ** k) / math.factorial(k)