from math import sqrt

while True:
    num = int(input("number: "))

    if num < 0:
        print("Invalid number")
        continue

    if num > 0:
        print(sqrt(num))
        continue

    elif num == 0:
        print("Exiting...")
        break
    
