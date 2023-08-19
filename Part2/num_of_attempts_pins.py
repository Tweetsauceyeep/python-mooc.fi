#Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes.

attempts = 0

while True:
    code = input("please type in your pin: ")
    attempts +=1

    if code == '4321' and attempts == 1:
        success = True
        break

    if attempts > 1 and code == '4321':
        success = False
        break

    # printed coz incorrect

    print("Wrong")

if success:
    print("Correct! It only took you one single attempt!")
elif success == False:
    print(f"Correct! It took you {attempts} attempts")

