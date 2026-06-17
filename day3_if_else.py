# Day 3 - Age Classification Program

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"\nHello, {name}!")

if age < 0:
    print("Invalid age.")
elif age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Extra information
years_to_100 = 100 - age

if years_to_100 > 0:
    print(f"You will turn 100 in {years_to_100} years.")
elif years_to_100 == 0:
    print("You are exactly 100 years old!")
else:
    print(f"You turned 100 {-years_to_100} years ago.")
    