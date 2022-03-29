#from tests.test_wave_01 import LETTER_POOL
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

SCORE_DICT = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z'],
}

def draw_letters():
    # generate list containing all letters
    # in corresponding frequency
    all_letters = []
    for letter,frequency in LETTER_POOL.items():
        for i in range(frequency):
            all_letters.append(letter)
    hand = []
    for i in range(10):
        # use random module to select one random
        #letter from list 
        this_letter = random.choice(all_letters)
        hand.append(this_letter)
        #update list to remove selected letter
        # using .remove() method
        all_letters.remove(this_letter)
        #repeat 10 times
    return hand

def uses_available_letters(word, letter_bank):
    word_bank = copy.deepcopy(letter_bank)
    caps_word = word.upper()
    for letter in caps_word:
        if letter not in word_bank:
            return False    
        else: 
            word_bank.remove(letter)    
    else:
    
        return True



def score_word(word):
    total = 0
    #look at each letter in word
    #add value associated with letter in dictionary to total
    for letter in word.upper():
        for value, letter_list in SCORE_DICT.items():
            if letter in letter_list:
                total += value

    if len(word) >= 7:
        total += 8
    return total

def get_highest_word_score(word_list):
    pass