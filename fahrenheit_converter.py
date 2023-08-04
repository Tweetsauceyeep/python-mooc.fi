# we tryna think programmatically here my senpai
# ask user for temp in Fahrenheit
# then print it out in Celsius
#if converted temperature falls below 0 deg celcius, then print brrr its cold blah blah kys

# my god my submission had errors but all i forgot was an exclamation mark 

temperature_f = int(input("Whats the temperature? "))

temperature_c = 5/9 * (temperature_f-32)


if temperature_c < 0:
    print(f"{temperature_f} degrees Fahrenheit equals {temperature_c} degrees Celsius")
    print("Brr! It's cold in here!")

else: 
    print(f"{temperature_f} degrees Fahrenheit equals {temperature_c} degrees Celsius")
