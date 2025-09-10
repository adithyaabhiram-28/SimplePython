def count(st):
    v,co = 0,0
    for c in st:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            v+=1
        else:
            co+=1
    return v,co

st = "fgasjcbkjhaoiwenpsojdfiowe"

print(count(st))