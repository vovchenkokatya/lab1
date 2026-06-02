def A(x, k):
    n = ((-1)**k) * (x**k)

    n = k**2 + k
    d = 1
    for i in range(1, n + 1):
        d *= i
    return n / d

if __name__ == '__main__':
    x = 2
    k = 3

    print(A(x, k))