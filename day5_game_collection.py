# Day 5 - Game Collection Manager

games = []

while True:
    print("\n=== Game Collection Manager ===")
    print("1. Add game")
    print("2. View games")
    print("3. Count games")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        game = input("Enter game name: ")
        games.append(game)
        print(f"{game} added successfully!")

    elif choice == "2":
        if len(games) == 0:
            print("No games in collection.")
        else:
            print("\nYour games:")
            for index, game in enumerate(games, start=1):
                print(f"{index}. {game}")

    elif choice == "3":
        print(f"You have {len(games)} games in your collection.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")