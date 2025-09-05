# no arg and no return 
def add1():
    a = 10
    b = 20
    c = a + b
    print(c)
add1()

# arg and no return
def add2(a,b):
    c = a + b
    print(c)
add2(100,200)

# no arg and return
def add3():
    a = 1000
    b = 2000
    c = a + b
    return c
print(add3())

# arg and return
def add4(a,b):
    c = a + b
    return c
print(add4(10000,20000))
