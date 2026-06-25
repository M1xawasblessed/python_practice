# Day 13 - Object-Oriented Programming (OOP)

class Player:

    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number

    def introduce(self):
        print(f"Player: {self.name}")
        print(f"Position: {self.position}")
        print(f"Shirt Number: {self.number}")


player1 = Player("Victor Osimhen", "Forward", 45)
player2 = Player("Lucas Torreira", "Midfielder", 34)

print("=== GALATASARAY PLAYERS ===\n")

player1.introduce()

print()

player2.introduce()