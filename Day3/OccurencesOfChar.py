def freq(st):
    s = set()
    res = ""
    for c in st:
        if c not in s:
            res = res + c + str(st.count(c))
            s.add(c)
    return res
st = "Hello World"
print(freq(st))