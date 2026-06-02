def sum(n):
    s = 0
    sign = 1 #знак

    for i in range(1, n + 1):
        s += sign / i
        sign = -sign
    return s

if __name__ == '__main__':
    n = 5

    print(sum(n))