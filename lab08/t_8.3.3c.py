def det(n, a):
    d0 = 1
    d1 = a

    if n == 1:
        return d1

    dn = 0
    for _ in range(2, n + 1):
        dn = a * d1 - d0
        d0 = d1
        d1 = dn
    return dn

if __name__ == '__main__':
    n = 5
    a = 2

    result = det(n, a)
    print(result)