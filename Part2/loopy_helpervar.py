### Example of using loops with helper variables
# program sues two helper variables: 
# variable keeps tracks of helper variables


attempts = 0

while True:
    code = input("please type in your pin: ")
    attempts +=1

    if code == '1234':
        success = True
        break

    if attempts == 3:
        success = False
        break

    # printed coz incorrect

    print("Incorrect...try again")

if success:
    print("Correct PIN entered!")
else:
    print("Too many attempts...")
