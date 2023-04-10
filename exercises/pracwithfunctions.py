
def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return("Too high of an index")
    #if we made it here, that means the letter_idx is valid
    return my_words[letter_idx]