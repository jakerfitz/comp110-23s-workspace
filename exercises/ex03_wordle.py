__author__ = "730474841"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(my_words: str, char: str) -> bool:
    """Outputs whether or not char is found in my_words"""
    assert len(char) == 1
    index: int = 0
    while len(my_words) >= (index + 1):
        if my_words[index] == char:
            return(True)
        index = index + 1
        if (index + 1) > len(my_words):
            return(False)
    return(False)

def emojified(guess: str, secret: str) -> str:
    """Outputs appropriate color wordle box for given input"""
    assert len(guess) == len(secret)
    index: int = 0
    empty: str = ""
    while (index < len(guess)):
        if secret[index] == guess[index]:
                empty = empty + GREEN_BOX
        elif contains_char(secret, guess[index]):
                empty = empty + YELLOW_BOX
        else:
            empty = empty + WHITE_BOX
        index = index + 1
    return(empty)

def input_guess(num_letters: int) -> str:
    guess = input(f"Enter a {num_letters} character word: ")
    while (len(guess) != num_letters):
        guess = input(f"That wasn't {num_letters} chars! Try again: ")
    return(guess)
    
def main() -> None:
    """The entrypoint of the program and main game loop."""
    num_guesses = 1
    codes = "codes"
    while num_guesses <= 6:
        print(f"=== Turn {num_guesses}/6 ===")
        result = input_guess(len(codes))
        print(emojified(result, codes))
        if emojified(result, codes) == (GREEN_BOX*5):
            print(f"You won in {num_guesses}/6 turns!")
            num_guesses = 7
        else:
            num_guesses = num_guesses + 1
    if num_guesses > 6 and (emojified(result, codes) != (GREEN_BOX*5)):
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()