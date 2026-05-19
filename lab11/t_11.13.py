def determinant_a(n):
    if n == 1:
        return 2
    if n == 2:
        return 3

    d_prev2 = 2
    d_prev1 = 3
    d_curr = 0

    for _ in range(3, n + 1):
        d_curr = 2 * d_prev1 - d_prev2
        d_prev2 = d_prev1
        d_prev1 = d_curr

    return d_curr

def determinant_b(n):
    if n == 1:
        return 3
    if n == 2:
        return 7
    d_prev2 = 3
    d_prev1 = 7
    d_curr = 0

    for _ in range(3, n + 1):
        d_curr = 3 * d_prev1 - 2 * d_prev2
        d_prev2 = d_prev1
        d_prev1 = d_curr

    return d_curr