"""One attempt to get the wordle"""

__author__ = "730474841"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")

while (len(guess) != len(secret)):
    new_guess = input(f"That was not {len(secret)} letters! Try again: ")
    guess = new_guess

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index = 0
empty = ""


if secret == guess:
        print(f"{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX}{GREEN_BOX} \nWoo! You got it!")
        exit()

while index < len(secret) and secret != guess:
        if secret[index] == guess[index]:
            empty = empty + GREEN_BOX
        else:
            found: bool = False
            count = 0
            while found != True and count < len(secret) and len(empty) != len(secret): 
                if secret[count] == guess[index]:
                    empty = empty + YELLOW_BOX
                    found = True
                else:
                    count = count + 1
            if found != True:
                empty = empty + WHITE_BOX
        index = index + 1

print(f"{empty} \nNot quite. Play again soon!")