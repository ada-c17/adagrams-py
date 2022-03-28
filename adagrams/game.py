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

import random
def draw_letters():
    list_of_distribution = []

    for key, val in LETTER_POOL.items():
        for i in range(val):
            list_of_distribution.append(key)
    
    letters_in_hand = []
    for i in range(1, 11):
        letter = random.choice(list_of_distribution)
        letters_in_hand.append(letter)
        list_of_distribution.remove(letter)
    
    # print("list of distribution: ",list_of_distribution)
    # print("letters in hand: ",letters_in_hand)
    return letters_in_hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass