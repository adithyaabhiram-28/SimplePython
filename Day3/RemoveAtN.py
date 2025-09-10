n = int(input("Enter the number of elements : "))

def remove(L,k):
    return L[:k]+L[k+1:]

L = []
for i in range(n):
    ele = int(input("Enter element : "))
    L = L + [ele]

print("Original List is :", L)
k = int(input("Enter the index to be removed : "))
print("List after removing element at index",k,"is :", remove(L,k))