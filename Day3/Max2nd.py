def SecondLargest(L):
    L.sort()
    return L[-2]

n = int(input("Enter the number of elements : "))
L = []
for i in range(n):
    ele = int(input("Enter element : "))
    L = L + [ele]

print("Second Largest is :", SecondLargest(L))