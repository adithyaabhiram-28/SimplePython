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
if isStrong(n):
    print(n, "is a Strong number")
else:
    print(n, "is not a Strong number")