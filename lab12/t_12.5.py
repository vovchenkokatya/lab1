def max_fibonacci(a):
    f0 = 0
    f1 = 1

    if a < 0:
        return None

    while f1 <= a:
        f_next = f0 + f1
        f0 = f1
        f1 = f_next
    return f0

if __name__ == '__main__':
    a = 10
    result = max_fibonacci(a)
    print(result)