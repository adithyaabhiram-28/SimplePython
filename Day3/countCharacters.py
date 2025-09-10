def count(st):
    a,n,s = 0,0,0
    for c in st:
        if c.isalpha():
            a+=1
        elif c.isdigit():
            n+=1
        else:
            s+=1
    return a,n,s

st = "6f!g5a^6g@j"

print(count(st))