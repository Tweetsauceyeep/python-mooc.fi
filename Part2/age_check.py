age = int(input("ur age? "))

if age >= 5:
    print(f"Ok, you're {age} years old")

elif age < 5 and age >= 0:
    print("I suspect you can't write quite yet...")

elif age < 0:
    print("That must be a mistake")

