# Day 8 - Error Handling

try:
    age = int(input("Enter your age: "))
    print(f"Next year you will be {age + 1} years old.")

except ValueError:
    print("Please enter a valid number!")