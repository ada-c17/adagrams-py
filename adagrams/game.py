import random
import copy

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
    '''This function returns 10 random letter tiles. Frequency of letters determined by LETTER_POOL'''
    letters = []
    letter_pool_copy = copy.deepcopy(LETTER_POOL)
    while len(letters) < 10:
        random_letter = random.choice(list(letter_pool_copy))
        if letter_pool_copy[random_letter] == 0:
            continue
        else:
            letters.append(random_letter)
            letter_pool_copy[random_letter] = letter_pool_copy[random_letter]-1
    return letters


    '''PSUEDOCODE:
    1) Make deep copy of LETTER_POOL
    2) if LETTER_POOL.deepcopy value = 0; remove
        3) Generate random letter from current LETTER_POOL.deepcopy- 
        4) Find letter in LETTER_POOL.deepcopy 
        5) -1 from value
        6) append letter to letters[]
    7) Return letters[]'''

def uses_available_letters(word, letter_bank):
    '''This function checks if all letters in a word are also available in the letter_bank'''
    valid_letters = []
    word = word.upper()
    letter_bank_copy =copy.deepcopy(letter_bank)
    for letter in word:
        if letter in letter_bank_copy:
            valid_letters.append(letter)
            letter_bank_copy.remove(letter)
    if len(valid_letters) == len(word):
        letter_bank_copy = letter_bank
        return True
    else:
        letter_bank_copy = letter_bank
        return False

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

print(draw_letters())