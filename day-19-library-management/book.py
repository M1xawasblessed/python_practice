# book.py

from item import Item


class Book(Item):
    def __init__(self, title, year, author, pages):
        if not author.strip():
            raise ValueError("Author cannot be empty")
        if pages <= 0:
            raise ValueError("Pages must be greater than 0")

        super().__init__(title, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"Book: {self.title} | {self.author} | {self.pages} pages | {status}"