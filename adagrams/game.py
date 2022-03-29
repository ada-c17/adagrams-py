# from tests.test_wave_01 import LETTER_POOL
from random import randint


from copy import deepcopy

LETTER_POOL = [
                "A", "A", "A", "A", "A", "A", "A", "A", "A",
                "B", "B",
                "C", "C",
                "D", "D", "D", "D", 
                "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
                "F", "F",
                "G", "G", "G",
                "H", "H",
                "I", "I", "I", "I", "I", "I", "I", "I", "I", 
                "J",
                "K",
                "L", "L", "L", "L", 
                "M", "M",
                "N", "N", "N", "N", "N", "N", 
                "O", "O", "O", "O", "O", "O", "O", "O", 
                "P", "P",
                "Q",
                "R", "R", "R", "R", "R", "R", 
                "S", "S", "S", "S", 
                "T", "T", "T", "T", "T", "T", 
                "U", "U", "U", "U", 
                "V", "V",
                "W", "W",
                "X",
                "Y", "Y",
                "Z"
    ]


def draw_letters():
    letter_pool_copy = deepcopy(LETTER_POOL)
    drawn_letters = []
    while len(drawn_letters) < 10:
        rand_index = randint(0, len(letter_pool_copy)-1)
        drawn_letters.append(letter_pool_copy.pop(rand_index))
    return drawn_letters




def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass