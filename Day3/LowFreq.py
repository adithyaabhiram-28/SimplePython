def low(st):
    ct = []
    s = set()
    for c in st:
        if c not in s:
            ct += [st.count(c)]
            s.add(c)
    return min(ct)

st = "Hello world"
print(low(st))