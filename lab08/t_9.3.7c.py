def det(n):
    d0 = 1
    d1 = 0

    if n == 1:
        return d1

    dn = 0
    for _ in range(2, n + 1):
        dn = d0
        d0 = d1
        d1 = dn
    return dn

if __name__ == '__main__':
    n = 98

    print(det(n))