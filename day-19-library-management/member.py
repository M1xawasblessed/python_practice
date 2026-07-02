# member.py

class Member:
    def __init__(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty")

        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item):
        if item.available:
            item.borrow()
            self.borrowed_items.append(item)

    def return_item(self, item):
        if item in self.borrowed_items:
            item.return_item()
            self.borrowed_items.remove(item)

    def show_items(self):
        if not self.borrowed_items:
            print("No borrowed items.")
        else:
            for item in self.borrowed_items:
                print(item)