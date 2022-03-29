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


#isolate the keys into thier own list
#isolate the values into their own list
#mulitply the two lists together
#import random
# use random sampling off the new list to choose the 10 letters
# return 10 letters


def draw_letters():
    letters = list(LETTER_POOL.keys())
    
    letter_quantity = list(LETTER_POOL.values())

    pool_strings = []

    pool = []

    for i in range(len(letters)):
        pool_strings.append(letters[i] * letter_quantity[i])

    for string in pool_strings:    
        for letter in string:
            pool.append(letter)

    letter_bank = list(random.sample(pool, 10))
    return letter_bank
            

print(draw_letters())

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass