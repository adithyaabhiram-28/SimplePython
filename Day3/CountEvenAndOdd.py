def count(L):
    e, o = 0, 0
    for i in L:
        if i % 2 == 0:
            e+=1
        else:
            o+=1
    return e, o

n = int(input("Enter the number of elements : "))
L = []
for i in range(n):
    ele = int(input("Enter element : "))
    L = L + [ele]

print("Even count and Odd count are :", count(L))