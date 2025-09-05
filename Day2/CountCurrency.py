n = int(input("Enter the amount: "))
def count(n):
    notes = [2000,500,200,100,50,20,10,5,2,1]
    count = {}
    for note in notes:
        count[note] = n // note
        n = n % note
    return count

print("Total number of notes:",count(n))