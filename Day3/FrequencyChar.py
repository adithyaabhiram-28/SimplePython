def count(st,ch):
    l = []
    for i,c in enumerate(st):
        if c == ch:
            l += [i]
    return l


st = "HelloWorld"
print(count(st,'l'))