""""6 Shot Wordle Exercise>"""

__author__ = "730523395"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, char: str) -> bool:
    """Finding a matching character at any index."""
    assert len(char) == 1 
    i: int = 0
    while i < len(word):
        if word[i] == char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Printing colored boxes correlating to the indexes."""
    assert len(guess) == len(secret) 
    counter: int = 0
    boxes: str = ""
    while counter < len(guess):
        if guess[counter] == secret[counter]:  
            boxes += GREEN_BOX
        elif contains_char(secret, guess[counter]) is True:
            boxes += YELLOW_BOX
        elif contains_char(secret, guess[counter]) is False:
            boxes += WHITE_BOX
        counter += 1
    return boxes


def input_guess(length_number: int) -> str:
    """Ensuring the guess word is the proper number of characters."""
    att_guess: str = ""
    att_guess = input(f"Enter a { length_number } character word: ")
    while length_number != len(att_guess):
        att_guess = input(f"That wasn't { length_number } chars! Try again: ")
    return att_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET = "codes"
    turns: int = 0
    won_game: bool = False
    guess: str = ""
    while (turns < 6) and won_game is False:
        if guess != SECRET:
            turns += 1
            print(f"=== Turn {turns}/6 ===")
            guess: str = input_guess(len(SECRET))
            boxes: str = emojified(guess, SECRET)
            print(boxes)
        else:
            won_game: bool = True
    
    if won_game:
        print(f"You won in { turns }/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    if __name__ == "__main__":
        main()

        
"""guess needs to be an empty string in order to call on imput_guess
later on in the function's body"""
"""I had trouble with the boolean and now I know 
I need to restate the bool = False/True to force the 
loop to quit"""
"""Lastly, to call on a function means to literally 
use how we called it in the termal and place that 
call into the functions body"""
"""These function calls can overlap where emojified
includes input_guess(guess) and then the next line 
print emojified literally aka boxes"""