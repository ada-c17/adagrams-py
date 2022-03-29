import random
import copy

def draw_letters():
    letters = random.sample(create_letter_pool_list(), 10)
    return letters

def create_letter_pool_list():
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
    letter_pool_list = []
    for letter in LETTER_POOL.keys():
        for frequency in range(LETTER_POOL[letter]):
            letter_pool_list.append(letter)
    return letter_pool_list

#check if letter is in letter bank
#if not, return false
#otherwise remove letter from letter bank and keep looping through letters in the word

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_bank_copy = copy.copy(letter_bank)
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    letter_point_table = {
        "A": 1,
        "E": 1,
        "I": 1,
        "O": 1,
        "U": 1,
        "L": 1,
        "N": 1,
        "R": 1,
        "S": 1,
        "T": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10
    }
    points = 0
    word = word.upper()
    for letter in word:
        points += letter_point_table[letter]
    if len(word) >= 7 and len(word) <= 10:
        points += 8
    
    return points

def get_highest_word_score(word_list):
    pass