"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730474841"

word = input("Enter a 5-character word: ")

if (len(word) < 5 or len(word) > 5):
    print("Error: Word must contain 5 characters")
    exit()
    
letter = input("Enter a single character: ")


print("Searching for " + letter + " in " + word)
if (word[0] == letter):
    print(letter + " found at index 0")
if (word[1] == letter):
    print(letter + " found at index 1")
if (word[2] == letter):
    print(letter + " found at index 2")
if (word[3] == letter):
    print(letter + " found at index 3")
if (word[4] == letter):
    print(letter + " found at index 4")

value = 0
if (word[0] == letter):
    value = value + 1
if (word[1] == letter):
    value = value + 1
if (word[2] == letter):
    value = value + 1
if (word[3] == letter):
    value = value + 1
if (word[4] == letter):
    value = value + 1

if (value == 0):
    print("No instances of " + str(letter) + " found in " + str(word))
if (value == 1):
    print(str(value) + " instance of " + str(letter) + " found in " + str(word))
if (value > 1):
    print(str(value) + " instances of " + str(letter) + " found in " + str(word))