def isPalindrome(s):
    return s == s[::-1]

n = int(input("Enter n: "))
for i in range(1, n + 1):
    if isPalindrome(str(i)):
        print(i, end=" ")