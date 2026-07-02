# tests.py

from book import Book
from magazine import Magazine
from member import Member

book = Book("Python", 2023, "Eric", 300)
assert book.available is True

book.borrow()
assert book.available is False

book.return_item()
assert book.available is True

mag = Magazine("Tech", 2024, 5)
assert mag.issue_number == 5

member = Member("Ayhan")
member.borrow_item(book)
assert len(member.borrowed_items) == 1

member.return_item(book)
assert len(member.borrowed_items) == 0

print("All tests passed!")