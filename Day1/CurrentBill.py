pres, last = map(int,input("Enter present and last month readings: ").split())
cname = input("Enter customer name: ")
cnum = input("Enter customer number: ")
units = pres - last
cost = units * 3
print("Customer Name:", cname)
print("Customer Number:", cnum)
print("Units Consumed:", units)
print("Total Bill Amount: Rs.", cost)