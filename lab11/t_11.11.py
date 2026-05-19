def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def check_fibonacci_primes(n):
    a, b = 1, 1
    print(f"{'n':<5} | {'F_n':<10} | {'Просте n?':<12} | {'Просте F_n?':<12} | {'Виконується умова?':<20}")
    print("-" * 65)

    for i in range(1, n + 1):
        prime_n = is_prime(i)
        prime_fn = is_prime(a)
        condition_met = True
        if prime_fn and not prime_n and i != 4:
            condition_met = False

        print(f"{i:<5} | {a:<10} | {str(prime_n):<12} | {str(prime_fn):<12} | {str(condition_met):<20}")
        a, b = b, a + b