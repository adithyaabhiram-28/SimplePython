n = int(input("Enter the number of elements : "))

def Frequency(L):
    D = {}
    for i in L:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
    return D

L = []
for i in range(n):
    ele = int(input("Enter element : "))
    L = L + [ele]
    
res = Frequency(L)
dup = 0
for key in res.keys():
    dup += res[key] - 1

print("Total count : ",dup)