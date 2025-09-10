def count_words(text):
    words = text.split()
    return len(words)

input = input("Enter a string: ")
total = count_words(input)
print(f"Total number of words: {total}")