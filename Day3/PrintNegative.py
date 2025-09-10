n = int(input("Enter the number of elements : "))

def printNegative(L):
    for i in L:
        if i < 0:
            print(i,end=" ")
            
L = []
for i in range(n):
    ele = int(input("Enter element : "))
    L = L + [ele]
    
printNegative(L)

