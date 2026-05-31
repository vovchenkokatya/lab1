import math

def fibonacci_generating_function(x, eps):
    limit = (math.sqrt(5) - 1) / 2
    if abs(x) >= limit or x == 0:
        return None, 0

    t_prev2 = 0
    t_prev1 = x

    s = t_prev2 + t_prev1
    n = 2
    term = x * t_prev1 + (x**2) * t_prev2

    while abs(term) >= eps:
        s += term
        t_prev2 = t_prev1
        t_prev1 = term
        term = x * t_prev1 + (x**2) * t_prev2
        n += 1
    return s, n

if __name__ == '__main__':
    x = 0.5
    eps = 0.000001

    approx_val, steps = fibonacci_generating_function(x, eps)

    print(approx_val)
