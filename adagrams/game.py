from random import choice, randint, shuffle
from copy import deepcopy

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

# create a list holding all 98 letters (letter_bank)
def create_letter_pool():
    letter_pool = []
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
            letter_pool.append(letter)
    
    return letter_pool

# thu's suggestion for improving draw_letters():
def draw_letters():

    # it will restart every time this function is invoked
    letter_pool = create_letter_pool()
    shuffle(letter_pool)
    user_hand = letter_pool[0:10]

    return user_hand

# tiffini
def uses_available_letters(word, letter_bank):
    
    # make a copy of letter bank list to avoid editing original list
    copy_of_letter_bank = deepcopy(letter_bank)

    # convert all letters in word to uppercase to allow for case insensitivity
    uppercase_word = word.upper()

    # check if each letter in upper_case word is in letter_bank
    # remove the letter if identified to update occurrence frequency in list, letter_bank
    for letter in uppercase_word:
        if letter not in copy_of_letter_bank:
            return False
        else:
            copy_of_letter_bank.remove(letter)
    
    return True



def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass