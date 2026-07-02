# magazine.py

from item import Item


class Magazine(Item):
    def __init__(self, title, year, issue_number):
        super().__init__(title, year)
        self.issue_number = issue_number

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"Magazine: {self.title} | Issue #{self.issue_number} | {status}"