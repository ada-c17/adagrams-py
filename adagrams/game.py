
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

letter_point ={
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K"): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10
}

import random


def draw_letters():
    """Drawing 10 letters from a pool of letter and return a list of that letters"""
    # a list to store all letters from a pool of letter
    list_letter = []
    # loop over LETTER_POOL to get key and value
    # key will be the letter adding to list and 
    # value is number of times that the letter will be adding
    for letter, count in LETTER_POOL.items():
        # adding letter into list depend on value of count 
        for i in range(count):
            list_letter.append(letter)
    # create a list that randomly draw 10 letters from list_letter 
    letter_draw = random.sample(list_letter, k=10)
    
    return letter_draw


def uses_available_letters(word, letter_bank):
    """
    Checking each letter of word:
        - return False if it is not in letter_bank
        - return True if it is in letter_banks
    """
    # create a new list which same as letter_bank, so it doen't effect to original when editing
    letter_bank_copy = letter_bank.copy()
    # loop over word to get each character
    for char in word.upper():
        # return False if the character of word not in the new created list
        if char not in letter_bank_copy:
            return False
        # otherwise removing each character of word from letter_bank_copy when it is in there
        # return True after removing all characters of word that is in letter_bank_copy
        else: 
            letter_bank_copy.remove(char)
    return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass