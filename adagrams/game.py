from random import shuffle
from adagrams import LETTER_POOL

def create_letter_pool():
    letter_pool = []
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
            letter_pool.append(letter)
    
    return letter_pool

def draw_letters():

    letter_pool = create_letter_pool()
    shuffle(letter_pool)
    user_hand = letter_pool[0:10]

    return user_hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass