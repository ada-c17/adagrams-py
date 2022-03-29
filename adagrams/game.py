import random
import copy
from re import L
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

def draw_letters():

    letter_pool_copy = copy.deepcopy(LETTER_POOL)
    drawn_letters = []

    for i in range(10):
        letter = random.choice(list(letter_pool_copy.keys()))
        if letter_pool_copy[letter] == 1:
            del letter_pool_copy[letter]       
        else:
            letter_pool_copy[letter] -= 1
        drawn_letters.append(letter)
    return drawn_letters

def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.deepcopy(letter_bank)
    for char in word:
        char = char.capitalize()
        if char in letter_bank_copy:
            letter_bank_copy.remove(char)
        else:
            return False
    return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass