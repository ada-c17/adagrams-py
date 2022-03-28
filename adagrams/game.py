
import random
import copy 

letter_pool = {
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
    user_pool = copy.deepcopy(letter_pool)
    letters = [] 
    while len(letters)< 10: 
        draw = random.choice(list(user_pool))
        for letter, count in user_pool.items():
            if user_pool[letter] == 0:
                continue 
            if letter == draw: 
                letters.append(draw) 
                user_pool[letter] -= 1 
                
    return letters 


def uses_available_letters(word, letter_bank):
    '''
    word = 'some word'
    letter_bank = draw_letters()
    return TRUE or FALSE 

    for letter in word: 
        if letter not in letter_bank: 
            return FALSE
        else: 
            if letter in letter_bank: 
                if word has same letter more than once, letter_bank must also! 
    
    '''
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass