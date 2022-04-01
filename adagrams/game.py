import random
""" Give us access to pick random object. We used this module to generate a randon
letter from string.ascii_uppercase in order to create our hand of letters."""
import string 
"""Gives us access to constants. We wanted to use the string.ascii_uppercase
method to access the upper case alphabet. We wanted to make sure all our inputs
changed into uppercase letters. """
SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def draw_letters():
    LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
    player_hand = []
    random_letter = ""
    while len(player_hand) < 10:
        random_letter = random.choice(string.ascii_uppercase)        
        if LETTER_POOL[random_letter] == 0:
            continue
        else:
            player_hand.append(random_letter)
            LETTER_POOL[random_letter] -= 1        
    return player_hand

def uses_available_letters(word, letter_bank):
    list_of_letters = letter_bank[:]
    bool_set = set()
    for letter in word.upper():
        if letter in list_of_letters:
            bool_set.add(True)
            list_of_letters.remove(letter)
        else:
            bool_set.add(False)


    if bool_set == {True}:
        return True
    else:
        return False

def score_word(word):
    score = 0
    for letter in word:
        score += SCORE_CHART[letter.upper()]
    if len(word) >= 7:
        score += 8
    return score


def get_highest_word_score(word_list):
    highest_score = 0
    winning_word = ""

    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            winning_word = word
            highest_score = score
        elif score == highest_score:
            if len(winning_word) == 10:
                continue
            elif len(word) == 10:
                winning_word = word
            elif len(word) < len(winning_word):
                winning_word = word
    return (winning_word, highest_score)