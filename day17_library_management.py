# Day 17 - Library Management System

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} - {self.author} ({status})")


library = []

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        title = input("Book Title: ")
        author = input("Author: ")

        library.append(Book(title, author))

        print("Book added successfully!")

    elif choice == "2":

        if not library:
            print("Library is empty.")
        else:
            print("\n===== BOOK LIST =====")
            for index, book in enumerate(library, start=1):
                print(f"{index}. ", end="")
                book.display()

    elif choice == "3":

        if not library:
            print("Library is empty.")
            continue

        number = int(input("Book number: ")) - 1

        if 0 <= number < len(library):
            if library[number].available:
                library[number].available = False
                print("Book borrowed successfully!")
            else:
                print("This book is already borrowed.")
        else:
            print("Invalid selection.")

    elif choice == "4":

        if not library:
            print("Library is empty.")
            continue

        number = int(input("Book number: ")) - 1

        if 0 <= number < len(library):
            library[number].available = True
            print("Book returned successfully!")
        else:
            print("Invalid selection.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")