search_word = input("Enter the word to search for: ")

# Initialize the number of guesses
guesses = 0

# Allow the user to guess the word
while guesses < 5:
    guess = input("Enter your guess: ")
    if len(guess.split()) > 5:
        print("Your guess must have 5 words or fewer. Try again.")
        continue
    if guess == search_word:
        print("Correct! You found the word.")
        break
    else:
        print("Incorrect. The following letters match:")
        for i in range(min(len(guess), len(search_word))):
            if guess[i] == search_word[i]:
                print(f"{i + 1}: {guess[i]}")
        print("Try again.")
        guesses += 1

if guesses == 5:
    print("Sorry, you have used all your guesses. The word was:", search_word)


    #def mimic(my_words: str) -> str:
    #"""Given the string my_words, outputs the same string"""
   # return(my_words)

#my_words: str = "Hello!"
#response: str = mimic(my_words)
#print(response)