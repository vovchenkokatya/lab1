def max(a):
    if a < 0:
        return None, None

    x0 = 1
    x1 = 0
    x2 = 1

    if a == 0:
        return 0, 1

    n = 2
    max_val = x2
    max_n = n

    while True:
        x_next = 2 * x2 + 3 * x0
        if x_next > a:
            break

        n += 1
        max_val = x_next
        max_n = n
        x0 = x1
        x1 = x2
        x2 = x_next

    return max_val, max_n

if __name__ == '__main__':
    a = 10
    val, index = max(a)
    print(val)
    print(index)