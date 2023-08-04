# calculate end of year bonus customer receives on their loyalty card
# bonus is calculated w/ the formula:
# if there is less than a hundred points on the card, the bonus is 10%
# in any other case: the bonus is 15% 

# Fix the program
# man completely not like da model formula and stuff 
# this worked but its not the model solution: probably because they havent introduced elif yet LMAO
# points = int(input("How many points are on your card? "))
# if points < 100:
#     points *= 1.1
#     print("Your bonus is 10 %")

# elif points >= 100:
#     points *= 1.15
#     print("Your bonus is 15 %")
# print("You now have", points, "points")

# how tf does this work mehn
points = int(input("How many points are on your card? "))
if points < 100:
    bonus = 1.1
    print("Your bonus is 10 %")

elif points >= 100:
    bonus = 1.15
    print("Your bonus is 15 %")

points *= bonus
print("You now have", points, "points")

