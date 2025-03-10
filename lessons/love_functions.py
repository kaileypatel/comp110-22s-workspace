"""Some examples of tender, loving function definitions."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"
 

def spread_love(to: str, n: int) -> str:
    """Generated a strong that repats a loving message n times."""
    love_note: str = ""
    counter: int = 0
    while counter < n:
        love_note += love(to) + "\n" 
        counter += 1 
    return love_note