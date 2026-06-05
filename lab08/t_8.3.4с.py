def determinant(n):
    D1 = 1
    D2 = -2
    for i in range(1, n+1):
        D3 = 5 * D2 - 6 * D1
        yield D1
        D1 = D2
        D2 = D3

if __name__ == '__main__':
    for item in determinant(5):
        print(item)