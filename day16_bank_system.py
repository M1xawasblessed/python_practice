# Day 16 - Bank Management System

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def show_balance(self):
        print(f"\nCurrent Balance: €{self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"\n€{amount} deposited successfully!")
        else:
            print("\nInvalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("\nInvalid amount.")
        elif amount > self.__balance:
            print("\nInsufficient balance.")
        else:
            self.__balance -= amount
            print(f"\n€{amount} withdrawn successfully!")


owner = input("Enter account owner's name: ")
account = BankAccount(owner)

while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Show Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        account.show_balance()

    elif choice == "2":
        amount = float(input("Deposit Amount: "))
        account.deposit(amount)

    elif choice == "3":
        amount = float(input("Withdraw Amount: "))
        account.withdraw(amount)

    elif choice == "4":
        print("\nThank you for using our bank system.")
        break

    else:
        print("\nInvalid option.")