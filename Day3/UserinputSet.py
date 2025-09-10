n = int(input("Enter size: "))
s = set()
for i in range(n):
    x = int(input(f"Enter number {i + 1}: "))
    s = s | {x}
print(s)