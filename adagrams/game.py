
from operator import is_
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
    'Z': 1}

SCORE_DICT= {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1,
    'P': 3,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'W': 4,
    'X': 8,
    'Y': 4,
    'Z': 10}


def draw_letters():
    pool_list = []
    # we are creating a pool list to make sure we stick to the right frequency
    for letter, frequency in LETTER_POOL.items():
        pool_list += letter * frequency
    
    random_letters_list = random.sample(pool_list, 10)
    return random_letters_list


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
    sum_scores = 0
    word = word.upper()
    for letter in word:
        sum_scores += SCORE_DICT[letter]
    if len(word) == 7 or len(word) == 8 or len(word) == 9 or len(word) == 10:
        sum_scores += 8
    return sum_scores


def get_highest_word_score(word_list):
    
    max_score = 0
    max_score_word = None
    for word in word_list:
        score = score_word(word)
        if score > max_score:
            max_score = score
            max_score_word = word
        elif score == max_score and len(max_score_word) != 10:
            if len(word) < len(max_score_word):
                max_score_word = word
            elif len(word) == 10:
                max_score_word = word
                
    return max_score_word, max_score
