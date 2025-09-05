def isArmstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return sum == num

n = int(input("Enter n: "))
for i in range(1, n + 1):
    if isArmstrong(i):
        print(i, end=" ")