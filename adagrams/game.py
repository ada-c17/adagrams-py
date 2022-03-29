
from operator import is_
import random


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
    'Z': 1}


def draw_letters():
    pool_list = []
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
            pool_list.append(letter)
    
    random_letters_list = random.sample(pool_list, 10)
    return random_letters_list

import copy
def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.deepcopy(letter_bank)
    for letter in word:
        letter = letter.upper()
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass