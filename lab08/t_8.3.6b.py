def sum(n):
    a = 1
    s = a

    for k in range(1, n + 1):
        n = n * 2 / (2 * k + 1)
        s += a
    return s

if __name__ == '__main__':
    n = 5
    print(sum(n))