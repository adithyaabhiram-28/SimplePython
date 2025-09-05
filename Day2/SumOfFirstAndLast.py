n = int(input("Enter a number: "))

f = n % 10
while n >= 10:
    n = n // 10
l = n
print("Sum of first and last digit is:", l + f)