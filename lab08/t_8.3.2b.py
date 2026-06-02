def calculate_product(n):
    p = 1
    for i in range(1, n + 1):
        p *= (i + 1) / (i + 2)
    return p

if __name__ == '__main__':
    n = 5
    result = calculate_product(n)

    print(result)