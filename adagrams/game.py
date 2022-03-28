import random

# from tests.test_wave_01 import LETTER_POOL
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
    '''
    1) importing the random module
    2) make each letter-value pair an element in a tuple/list?
        put values of the letters in a list (Like 9 A's in a list, 2 B's)
    3) a method from the random module to shuffle the list
    4) list comprehension
    '''
    letters = []
    for letter, number in LETTER_POOL.items():
        for i in range(number):
            letters.append(letter)
    random.shuffle(letters)
    return letters[:10]

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass