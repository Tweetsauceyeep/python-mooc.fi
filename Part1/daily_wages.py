# ask for hourly wage
# ask for hours worked
# day of the week

hour_wage = float(input("Hourly wage "))
hours_worked= float(input("Hours worked "))
day = input("day of the week? ")

if day.capitalize() == "Sunday":
    hour_wage *= 2

total_wage = hour_wage * hours_worked
print(f"Daily wages: {total_wage} euros")

# how to do with no else statement
# hourly_wage = float(input("Hourly wage: "))
# hours_worked = int(input("Hours worked: "))
# weekday = input("Day of the week: ")
# if weekday == "Sunday":
#     hourly_wage *= 2
# total_wage = hourly_wage * hours_worked
# print(f"Daily wages: {total_wage} euros")
