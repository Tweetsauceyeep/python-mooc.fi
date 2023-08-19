password = input("Password: ")
while True:
    repeat_password = input("Repeat Password: ")
    if repeat_password == password:
        break
    elif repeat_password != password:
        print("They do not match!")

print("User account created!")
