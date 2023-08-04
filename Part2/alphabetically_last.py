word1 = input("first word ")
word2 = input("second word ")

if word1 < word2:
    print(f"{word2} comes alphabetically last.")
elif word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word1 == word2:
    print("You gave the same word twice.")
