# Calculator Example
# Date: August 3, 2023

number1 = float(input("first number "))
number2 = float(input("second number "))
operation = input("operation ")

if operation == "add":
    print(f"{number1} + {number2} = {number1 + number2}")
if operation == "multiply":
    print(f"{number1} * {number2} = {number1 * number2}")
if operation == "subtract":
    print(f"{number1} - {number2} = {number1 - number2}")
if operation == "divide":
    print(f"{number1} / {number2} = {number1 / number2}")
