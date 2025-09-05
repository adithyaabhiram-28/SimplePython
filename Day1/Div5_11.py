def div(n):
    if n % 5 == 0 and n % 11 == 0:
        return True
    else:
        return False

n = int(input("Enter a number: "))
print(div(n))