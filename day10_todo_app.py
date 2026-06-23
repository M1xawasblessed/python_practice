# Day 10 - To-Do List App

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        print("Task added!")

    elif choice == "2":
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()

                if len(tasks) == 0:
                    print("No tasks found.")
                else:
                    print("\nYour Tasks:")
                    for index, task in enumerate(tasks, start=1):
                        print(f"{index}. {task.strip()}")

        except FileNotFoundError:
            print("No tasks file found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")