def sum(n):
    a1 = 1
    a2 = 1
    a3 = 1

    s = 0
    pow2 = 2

    for k in range(1, n + 1):
        if k == 1:
            ak = a1
        elif k == 2:
            ak = a2
        elif k == 3:
            ak = a3
        else:
            ak = a3 + a1

            a1 = a2
            a2 = a3
            a3 = ak
        s += ak / pow2
        pow2 *= 2
    return s

if __name__ == '__main__':
    n = 5

    print(sum(n))