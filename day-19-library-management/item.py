# item.py

class Item:
    def __init__(self, title, year):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        if year < 1450:
            raise ValueError("Year must be 1450 or later")

        self.title = title
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False

    def return_item(self):
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} ({self.year}) - {status}"