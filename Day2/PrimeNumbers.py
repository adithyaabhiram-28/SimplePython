def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_upto_n(n):
    return [x for x in range(1, n + 1) if is_prime(x)]

n = int(input("Enter n: "))
primes = prime_numbers_upto_n(n)
print(f"Prime numbers from 1 to {n}: {primes}")