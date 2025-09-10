class Store:
    def __init__(self):
        self.prod = []
        self.c = 0
    def add(self,item):
        self.prod.append(item)
        self.c += 1
    def search(self,item):
        return (item in self.prod)
    def remove(self,item):
        self.prod.remove(item)
        self.c -= 1
    def count(self):
        return self.c
    def display(self):
        self.prod.sort()
        print(self.prod)
    def clear(self):
        del self.prod
    

n = int(input("Enter number of items in cart: "))
prod = Store()
for i in range(n):
    item_name = input("Enter item name: ")
    prod.add(item_name)
prod.display()
m = int(input("Enter number of items in cart: "))
for i in range(m):
    item_name = input("Enter item name: ")
    prod.remove(item_name)
prod.display()
item_name = input("Enter item name: ")
print(f"Is {item_name} present?",prod.search(item_name))
print("Total number of items are : ",prod.c)
