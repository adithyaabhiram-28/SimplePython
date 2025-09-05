def year(n):
    if (n%4 == 0 and n%100 != 0) or (n%400 == 0):
        return True
    else:
        return False
n = int(input("Enter a year: "))

if year(n):
    print(f"{n} is a leap year.")
else:
    print(f"{n} is not a leap year.")