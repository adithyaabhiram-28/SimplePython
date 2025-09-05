import math

def isStrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += math.factorial(digit)
        temp //= 10
    return sum == n

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if isStrong(i):
        print(i, end=" ")