'''
You are building a Library Management System in Python. The system should store books in a dictionary where:
Key → Book ID
Value → Book Title
Write a Python program to perform the following operations using Dictionaries:
Add a book to the library (Book ID, Title).
Remove a book using Book ID.
Search for a book by Book ID and display the title.
Update the title of a book (e.g., correction in title).
Display all books in the library.
Count the total number of books in the library.
Check if a book title exists in the library (reverse lookup).
'''

class Library:
    def __init__(self):
        self.books = {}
    def add(self,name,id):
        self.books[id] = name
    def update(self,name,id):
        self.add(name,id)
    def count(self):
        return len(self.books)
    def remove(self,id):
        removed = self.books.pop(id, None)
        if removed:
            print(f"Book with ID {id} removed")
        else:
            print("Book ID not found")
    def searchId(self,id):
        if id in self.books:
            print(f"{self.books[id]} is present")
        else:
            print("Book not present")
    def display(self):
        for k,v in self.books.items():
            print(f"{k} : {v}")
    def searchName(self,name):
        if name in self.books.values():
            print(f"{name} is present")
        else:
            print("Book not present")


lib = Library()

while True:
    print("\n====== Library Menu ======")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Remove Book")
    print("4. Search Book by ID")
    print("5. Search Book by Name")
    print("6. Display All Books")
    print("7. Count Books")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        id = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        lib.add(name, id)
        print("Book added successfully!")
    elif choice == "2":
        id = input("Enter Book ID to update: ")
        name = input("Enter new Book Name: ")
        lib.update(name, id)
        print("Book updated successfully!")

    elif choice == "3":
        id = input("Enter Book ID to remove: ")
        lib.remove(id)

    elif choice == "4":
        id = input("Enter Book ID to search: ")
        lib.searchId(id)

    elif choice == "5":
        name = input("Enter Book Name to search: ")
        lib.searchName(name)

    elif choice == "6":
        lib.display()

    elif choice == "7":
        print(f"Total books: {lib.count()}")

    elif choice == "8":
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 8.")