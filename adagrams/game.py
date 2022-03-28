import string
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
    'Z': 1
}

def draw_letters():
    list_letter = []
    for letter, count in LETTER_POOL.items():
        for i in range(0, count):
            list_letter.append(letter)
    letter_draw = random.sample(list_letter, k=10)
    
    return letter_draw


def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    for char in word.upper():
        if char not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(char)
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass