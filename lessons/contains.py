"""Example of writing a function to process a list."""


def main() -> None:
    guess: str = input("What is the code word? ")
    possible_answers: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("We're letting you in the secret club...")
    else:
        print("Go back to Davis.")

# Define a function named contains 
# parameters: 
#   1. needle - the str we're searching for
#   2. haystack - the list of str values we're searching through


def contains(needle: str, haystack: list[str]) -> bool:
    """"Test if needle is found in haystack."""
# Algorithm: for each item in haystack: 
#          Test if equal to the needle we're looking for 
#               If so, return True
    for item in haystack:
        if item == needle:
            return True
# After all items are check, that means needle not found, return False
    return False
# Returns True if needle is found in haystack


print(__name__)

if __name__ == "__main__":
    main()