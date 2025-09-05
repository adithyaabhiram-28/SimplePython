n = int(input("Enter a number: "))

f = n % 10
while n >= 10:
    n = n // 10
l = n
print("The first digit is:", l)
print("The last digit is:", f)