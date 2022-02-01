"""One Shot Wordle Exercise."""

__author__ = 730523395

SECRET = "python"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

word_count: int = 0 
boxes: str = "" 

guess = input(f"What is your { len(SECRET) } letter guess? ")

while len(guess) != len(SECRET):
    guess = input(f"That was not { len(SECRET) } letters! Try again: ")
    len(guess) == len(SECRET)

while word_count < len(SECRET):
    if guess[word_count] == SECRET[word_count]:
        boxes = boxes + GREEN_BOX
    elif guess[word_count] != SECRET[word_count]:
        letter_place = False
        alt: int = 0
        while not letter_place and alt < len(SECRET):
            if guess[word_count] == SECRET[alt]:
                letter_place = True
            else: 
                letter_place = False
            alt += 1
        if letter_place:
            boxes = boxes + YELLOW_BOX
        else:
            boxes = boxes + WHITE_BOX
    word_count += 1
                         
if guess == SECRET:
    print(boxes)
    print("Woo! You got it!")

if guess != SECRET:
    print(boxes)
    print("Not quite. Play again soon!")

"""If the word_count is in this case between 0-5 which is the index, 
then the loop follors with wheter the guessed word is equal to the secret"""
"""If the guessed word is not EXACTLY the secret then it goes on the elif... notice the line-up
between if and elif"""
"""It gets tricky here... lets say we are comparing BOTHER and PYTHON: B does not equal P
we go straight into the while not statement becasue the letter_place and the alt are being initialized 
so each time the loop repeats, it is respectively false and zero(still a little fuzzy on 
how bool statements come into play"""
"""So the next part is saying while true AND true (equals to true because of one of those equals false
then it is ALL false)"""
"""Next is if the zero index of guess and zero index of secret are equal then bool is re-initialized
to True and if they arent and in this case B does not equal P, then bool or letter_place is false"""
"""Alt += 1 means to go to the next letter in python which is y and word_count += 1 does the same thing 
only with the guessed word and is at the end so the first word that is being dissected is python"""
"""As for the boxes, if the letter_count is true then there are yellow boxes signaling the letter
is somewhere in python or the secret word and else means there is zero matches and turns to white boxes"""