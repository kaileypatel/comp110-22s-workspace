"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730523395"


GUESS: str = input("Enter a 5-character word: ")

if len(GUESS) != int(5):
    print("Error: Word must contain 5 characters")
    exit()

GUESS2: str = input("Enter a single character: ")

if len(GUESS2) != int(1):
    print("Error: Character must be a single character. ")
    exit()

print("Searching for " + GUESS2 + " in " + GUESS)

count_word = 0

if GUESS[0] == GUESS2:
    print(GUESS2 + " found at index 0 ")
    count_word += 1
if GUESS[1] == GUESS2:
    print(GUESS2 + " found at index 1 ")
    count_word += 1
if GUESS[2] == GUESS2:
    print(GUESS2 + " found at index 2 ")
    count_word += 1
if GUESS[3] == GUESS2:
    print(GUESS2 + " found at index 3 ")
    count_word += 1
if GUESS[4] == GUESS2:
    print(GUESS2 + " found at index 4 ")
    count_word += 1
    
if count_word == 1:
    print(count_word, "instance of " + GUESS2 + " found in " + GUESS)
if count_word > 1:
    print(count_word, "instances of " + GUESS2 + " found in " + GUESS)
else:
    if count_word == 0: 
        print("No instances of " + GUESS2 + " found in " + GUESS)