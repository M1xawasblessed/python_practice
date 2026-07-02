# main.py

from library import Library
from book import Book
from magazine import Magazine
from member import Member

library = Library()

book1 = Book("Python Crash Course", 2023, "Eric Matthes", 550)
book2 = Book("Clean Code", 2008, "Robert C. Martin", 464)
book3 = Book("Fluent Python", 2022, "Luciano Ramalho", 1014)

mag1 = Magazine("Tech Monthly", 2025, 15)
mag2 = Magazine("Science Today", 2025, 8)

library.add_item(book1)
library.add_item(book2)
library.add_item(book3)
library.add_item(mag1)
library.add_item(mag2)

member1 = Member("Ayhan")
member2 = Member("Sara")

library.add_member(member1)
library.add_member(member2)

member1.borrow_item(book1)
member2.borrow_item(mag1)

library.show_items()

print()

library.show_members()

print()

member1.show_items()
print()
member2.show_items()

member1.return_item(book1)

print("\nAfter return:\n")
library.show_items()