def check_padovan(N):
    P = [1, 1, 1]
    for k in range(3, N + 1):
        P.append(P[k-2] + P[k-3])

    print(f"Послідовність Падована до {N}: {P}")

    for n in range(14, N + 1):
        a_ok = P[n] == P[n-1] + P[n-5]
        b_ok = P[n] == P[n-2] + P[n-4] + P[n-8]
        c_ok = P[n] == 2*P[n-2] - P[n-7]
        d_ok = P[n] == 4*P[n-5] + P[n-14]

        if not (a_ok and b_ok and c_ok and d_ok):
            print(f"Помилка для n={n}!")
            return False

    print("Всі рекурентні формули успішно перевірені для всіх n >= 14 та n <= N!")
    return True