# Conditional statements can also be nested within other conditional statements.
# For example, the following program checks whether a number is above zero, and then whether it is odd or even:

number = int(input("Please type in a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative or zero")
