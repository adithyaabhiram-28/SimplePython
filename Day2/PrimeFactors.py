n = int(input("Enter a number: "))

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, n + 1):
    if n % i == 0 and isPrime(i):
        print(i, end=" ")