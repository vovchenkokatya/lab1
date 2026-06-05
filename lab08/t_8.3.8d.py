def D(n, u, v):
    S = 0
    a = u
    b = v
    fact = 1

    for k in range(1, n + 1):
        fact *= (k + 1)
        if k > 1:
            a_prev = a
            b_prev = b
            a = 2 * b_prev + a_prev
            b = 2 * (a_prev ** 2) + b_prev

        S += (a * b) / fact
        yield S

if __name__ == '__main__':
    for item in D(5, 1, 1):
        print(item)