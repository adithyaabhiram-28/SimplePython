# Simple Interest
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))
si = (p * r * t) / 100
print("Simple Interest is:", si)
print("Total amount after interest is:", p + si)