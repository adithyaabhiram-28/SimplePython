def Perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if Perfect(i):
        print(i, end=" ")
        
