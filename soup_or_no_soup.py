name = input("what name ")
total_cost = 0

if name != "Jerry":
    soup_portions = int(input("how many portions of soup "))
    total_cost = soup_portions * 5.90
    print(f"The total cost is {total_cost}")

print("Next please!")
