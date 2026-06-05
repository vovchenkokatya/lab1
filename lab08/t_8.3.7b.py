def B(n):
    S = 0
    for k in range(2, n + 1):
        S += ((-1)**k) * (k - 1) / k
        yield S

if __name__ == '__main__':
    for item in B(5):
        print(item)