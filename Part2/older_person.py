person1_name = input("person 1 name")
person1_age = int(input("person 1 age"))
person2_name = input("person 2 name")
person2_age = int(input("person 2 age"))

if person1_age > person2_age:
    print(f"The elder is {person1_name}")
elif person2_age > person1_age:
    print(f"The elder is {person2_name}")
else:
    print(f"{person1_name} and {person2_name} are the same age")
