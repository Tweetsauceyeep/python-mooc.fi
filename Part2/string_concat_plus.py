# Concatenating strings with the + Operator
#A similar idea of incrementation works with string variables as well. The program could, for instance, keep track of all the PIN codes the user typed in:

codes = ""
attempts = 0

while True:
    code = input("Please type in your PIN: ")
    attempts += 1
    codes += code + ", "
    # ...
