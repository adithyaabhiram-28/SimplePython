def high(st):
    ct = 0
    s = set()
    for c in st:
        if c not in s:
            ct = max(st.count(c),ct)
            s.add(c)
    return ct

st = "Hello world"
print(high(st))