"""If it's raining, tell me to pack umbrella"""

weather: str = input("What is the weather like? ")

if (weather == "rain"):
    print("Pack an umbrella!")
    print("But don't be down just because it's a rainy day!")

else:
    if (weather == "snow"):
        print("Pack a jacket!")
    if (weather == "blizzard"):
        print("wowzaaaaa!")
    if (weather == "hale"):
        print("don't slip!")
    print("Be careful! Don't have too much fun!")
print("Have a lovely day")


"""extra work from ex02 i may or may not use...


    while secret[index] == guess[char] and secret != guess:
        if secret[index] = guess[char]
        print(f"{GREEN_BOX} \n Not quite. Play again soon!")
        index = index + 1
    if (secret[index] == guess[index]):
        print(GREEN_BOX)
    index = index + 1
    
    """