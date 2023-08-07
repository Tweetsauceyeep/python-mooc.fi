name = input("Please type in your name")

if name.capitalize() == "Huey" or name.capitalize() == "Dewey" or name.capitalize() == "Louie":
    print("I think you might be one of Donald Duck's nephews.")

elif name.capitalize() == "Morty" or name.capitalize() == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")

else:
    print("You're not a nephew of any character I know of.")
