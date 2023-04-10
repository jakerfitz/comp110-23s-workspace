"""This is a game to predict whether someone is more like Mario or Luigi."""
import random

__author__ = "730474841"

VIDEOGAME_EMOJI: str = "\U0001F3AE"

points: int = 0
player: str = ""

STATEMENTS: list[str] = ["I like to be the first to go out and adventure!", "I like being the center of attention!", "I am viewed as someone who is a leader.", "I like the color red more than green"]


def greet() -> None:
    """This is a greeting for the player, and assigns the user's name to the player."""
    global player
    """Greeting for player"""
    print("Find out if you are an more like Mario or Luigi!")
    player = input("What's your name? ")
    print(f"Hello, {player}! Let's see who you are!")


def add_interaction() -> None:
    """Asks if user is comfortable with questions & acts as custom procedure."""
    answer = input("Are you comfortable answering questions about your personality? ('Y' for Yes / 'N' for No). ")
    if answer == "Y":
        print(f"Awesome {player}, let's go on then!")
    if answer == "N":
        print(f"No worries {player}! Have a nice day!")
        exit()
    if (answer != "Y") and (answer != "N"):
        print("I don't understand your response, I'll take that as a yes.")
      

def if_you_identify() -> int:
    """Sets up options for the player being more similar to Mario or Luigi."""
    global points
    statement = random.choice(STATEMENTS)
    print(f"Statement: {statement}")
    userselects = input("Identify with or without the given statement (by typing 'Y' or 'N' or typing 'Q' to quit playing): ")
    if userselects == "Q":
        return
    if userselects == "Y":
        points += 1
        print(f"Okay, interesting {player}!")
    if userselects == "N":
        points -= 1
        print(f"Okay, interesting {player}!")
    return points


def who_you_are(points: int) -> int:
    """Helps to figure out which one they are most similar to based on two questions."""
    if points > 0:
        print(f"{player}, you're more similar to Mario! {VIDEOGAME_EMOJI}")
    elif points < 0:
        print(f"{player}, you're more similar to Luigi! {VIDEOGAME_EMOJI}")
    else:
        print("One more question to see who you are most similar to!")
        points += if_you_identify()
        if points > 0:
            print(f"{player}, you're more similar to Mario! {VIDEOGAME_EMOJI}")
        if points < 0:
            print(f"{player}, you're more similar to Luigi! {VIDEOGAME_EMOJI}")
    return points


def path_one() -> int:
    """This path is a random small positive integer assigned as Mario that's arbitrarily associated with the first path."""
    print("You chose path one!")
    random_points = random.randint(0, 2)
    return random_points


def path_two() -> int:
    """This path is a random small negative integer representing more of Luigi which has been associated with following the second path."""
    print("You chose path two!")
    random_points = random.randint(-2, 0)
    return random_points


def main() -> None:
    """Creates the actual game or wtvr."""
    greet()
    global points
    add_interaction()
    points = if_you_identify()
    points += if_you_identify()
    while True:
        print(f"{player}, where would you like to go next?")
        print("1. Path one.")
        print("2. Path two.")
        print("3. Path three... mind you this takes you out of the game!")
        chosen_path = input(f"{player}, which do you select (input either 1, 2, or 3)? ")
        if chosen_path == "1":
            points += path_one()
        elif chosen_path == "2":
            points += path_two()
        elif (chosen_path == "3"):
            print(f"Goodbye {player}, your total final points are {points}")
            quit()
        else:
            print("Invalid Response")
        points = who_you_are(points)
        print(f"your total final points are {points}")
        quit()


if __name__ == "__main__":
    main()