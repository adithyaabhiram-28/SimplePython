def preLetterCase(s,c):
    res = ""
    j = 0
    for i in s:
        if i == c.lower() or i == c.upper():
            break
        j += 1
    res = s[:j].lower() + s[j:].upper()
    return res
print(preLetterCase("KeeP trying", "p"))


