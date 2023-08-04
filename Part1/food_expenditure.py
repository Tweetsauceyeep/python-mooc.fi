## mooc.fi programming exercise
## link: https://programming-23.mooc.fi/part-1/4-arithmetic-operations

# write a program which estimates a user's typical food expenditure
# how many times a week they eat at the student cafeteria
# ask for price of a student lunch
# money spent on groceries during the week
# then calculates the user's typical expenditure both weekly and daily

meals_week = int(input("how many times a week do you eat at the cafeteria "))
lunch_price = float(input("how much is the typical student lunch "))
grocery_spent = float(input("how much money do you spend on groceries in a week "))

#((2.5 * 4) +28.5)/7
#daily_expenditure = ((meals_week * lunch_price) + grocery_spent)/7
# can be changed to this to make it betta
weekly_expenditure = (lunch_price * meals_week) + grocery_spent
daily_expenditure = weekly_expenditure/7

print("Average food expenditure:")
print(f"Daily: {daily_expenditure} euros")
print(f"Weekly: {weekly_expenditure} euros")
