# from tests.test_wave_01 import LETTER_POOL
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
    '''
    1) import the random module and make LETTER_POOL a global variable
    2) how should we iterate through the LETTER_POOL?
        a) make each letter-value pair a dictionary as an element in a tuple/list?
        B) put values of the letters in a list (Like nine A elements, two B elements, etc.)
    3) use a method from the random module to shuffle the list
    4) return the first 10 elements in the shuffled list
    '''
    # letters = []
    # for letter, number in LETTER_POOL.items():
    #     for i in range(number):
    #         letters.append(letter)

    letters = [letter for letter, letter_frequency in LETTER_POOL.items() for number in range(letter_frequency)]

    random.shuffle(letters)

    return letters[:10]

def uses_available_letters(word, letter_bank):
    '''
    1) How do get the right quanities in letter_bank?
        A) Use a helper function?
        B) Iterate over the list, make a new list, and subtract?
        C) Set subtraction? NO
        D) Use letter_bank to determine frequency
    2) 
    3) 
    '''
    # word_list = list(word)
    # new_list = []
    # for letter in word:
    #     for i in range(len(letter_bank) - 1):
    #         if 
            
    # print(word_list)

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass