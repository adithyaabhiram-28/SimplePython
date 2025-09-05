pres, last = map(int,input("Enter present and last month readings: ").split())
cname = input("Enter customer name: ")
cnum = input("Enter customer number: ")
units = pres - last
cost = units*3

def cal1(u):
    return u*3.80
def cal2(u):
    return u*4.20
def cal3(u):
    return u*5.10
def cal4(u):
    return u*6.30
def cal5(u):
    return u*7.50

if units in range(0,51):
    cost = cal1(units)
elif units in range(51,101):
    cost = cal1(50) + cal2(units-50)
elif units in range(101,201):
    cost = cal1(50) + cal2(50) + cal3(units-100)
elif units in range(201,301):
    cost = cal1(50) + cal2(50) + cal3(100) + cal4(units-200)
else:
    cost = cal1(50) + cal2(50) + cal3(100) + cal4(100) + cal5(units-300)
    
print("Customer Name:", cname)
print("Customer Number:", cnum)
print("Units Consumed:", units)
print("Total Bill Amount: Rs.", cost)