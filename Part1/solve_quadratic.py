from math import sqrt

a = float(input("What is a? "))
b = float(input("What is b? "))
c = float(input("What is c? "))

d = b**2 - 4*a*c
positive_root = (-b + sqrt(d))/2*a
negative_root = (-b - sqrt(d))/2*a

print(f"The roots are {positive_root} and {negative_root}")

