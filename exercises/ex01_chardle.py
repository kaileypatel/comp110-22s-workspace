"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730523395"

guess: str = input("Enter a 5-character word: ")

if len(guess) != len("str!!"):
    exit("Error: Word must contain 5 characters")

guess2: str = input("Enter a single character: ")
print("searching for " + guess2 + " in " + guess)

if len(guess2) != len("s"):
    exit("Error: Character must be a single character.")

count_word = 0

if guess[0] == guess2:
    print(guess2 + " found at index 0 ")
    count_word += 1
if guess[1] == guess2:
    print(guess2 + " found at index 1 ")
    count_word += 1
if guess[2] == guess2:
    print(guess2 + " found at index 2 ")
    count_word += 1
if guess[3] == guess2:
    print(guess2 + " found at index 3 ")
    count_word += 1
if guess[4] == guess2:
    print(guess2 + " found at index 4 ")
    count_word += 1

if count_word == 0: 
    print("No instances of " + guess2 + " found in " + guess) 
if count_word == 1:
    print("1 instance of " + guess2 + " found in " + guess)
if count_word > 1: 
    print("2 instances of " + guess2 + " found in " + guess)
