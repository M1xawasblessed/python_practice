# library.py

class Library:
    def __init__(self):
        self.items = []
        self.members = []

    def add_item(self, item):
        self.items.append(item)

    def add_member(self, member):
        self.members.append(member)

    def show_items(self):
        for item in self.items:
            print(item)

    def show_members(self):
        for member in self.members:
            print(member.name)

    def find_item(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                return item
        return None