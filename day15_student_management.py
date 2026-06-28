# Day 15 - Student Management System

class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"\nName : {self.name}")
        print(f"Age  : {self.age}")
        print(f"Grade: {self.grade}")


students = []

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        name = input("Student Name: ")
        age = int(input("Student Age: "))
        grade = input("Student Grade: ")

        student = Student(name, age, grade)

        students.append(student)

        print("\nStudent added successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("\nNo students found.")

        else:
            print("\n===== Student List =====")

            for student in students:
                student.display_info()

    elif choice == "3":

        print("\nGoodbye!")
        break

    else:
        print("\nInvalid option!")