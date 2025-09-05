n = int(input("Enter a number: "))
p = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        p = False
        break
if p and n > 1:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")