"""One attempt to get the wordle."""

__author__ = "730474841"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")

while (len(guess) != len(secret)):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index = 0
empty = ""

while ((index < len(secret)) and (secret != guess)):
    if secret[index] == guess[index]:
        empty = empty + GREEN_BOX
    else:
        found: bool = False
        count = 0
        while ((found is False) and (count < len(secret))): 
            if secret[count] == guess[index]:
                empty = empty + YELLOW_BOX
                found = True
            else:
                count = count + 1
        if found is False:
            empty = empty + WHITE_BOX
    index = index + 1

if secret == guess:
    print(f"{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX} \nWoo! You got it!")
else:
    print(f"{empty} \nNot quite. Play again soon!")