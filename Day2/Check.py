c = input("Enter any character: ")

if c.isalpha():
    print("The character is an alphabet.")
elif c.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")