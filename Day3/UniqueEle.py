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

print("Unique elements are : ")
for key in res.keys():
    if res[key] == 1:
        print(key,end=" ")