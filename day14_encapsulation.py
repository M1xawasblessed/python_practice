# Day 14 - Encapsulation

class Player:

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary

    def show_player(self):
        print(f"Player: {self.name}")
        print(f"Position: {self.position}")

    def show_salary(self):
        print(f"Salary: €{self.__salary:,}")

    def update_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print("Salary updated successfully!")
        else:
            print("Invalid salary.")


player = Player("Victor Osimhen", "Striker", 12000000)

print("=== PLAYER INFORMATION ===")

player.show_player()

print()

player.show_salary()

print()

player.update_salary(15000000)

player.show_salary()