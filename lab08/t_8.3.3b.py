def A(n):
    S = 0
    a_prev2 = 1
    a_prev1 = 1
    power3 = 1

    for k in range(1, n + 1):
        power3 *= 3
        if k == 1:
            a_k = 1
        elif k == 2:
            a_k = 1
        else:
            a_k = (a_prev1 / k) + a_prev2
            a_prev2 = a_prev1
            a_prev1 = a_k

        S += power3 / a_k
        yield S

if __name__ == '__main__':
    for item in A(5):
        print(item)