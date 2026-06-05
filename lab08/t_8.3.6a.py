def generate(x, n):
    a = x
    yield a

    for k in range(1, n):
        a *= -x**2 / ((2 * k) * (2 * k + 1))
        yield a

if __name__ == '__main__':
    for item in generate(3, 10):
        print(item)