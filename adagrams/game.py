import random
import string
DRAWN_LETTERS_TOTAL = 10

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
    # randonly draw 10 letters, should match the letter pool rules
    # create a dictionary to keep track of our {current drawn letter : count}
    # update letter count in the dict
    # check if letter count is over LETTER_POOL[letter]
    # if yes, remove the letter
    # if no, do nothing
    # keep drawing until have 10 letters
    # returns an array of 10 letters
    result = []
    letter = ''
    drawn_letters = {}
    
    while len(result) < DRAWN_LETTERS_TOTAL:
        letter = random.choice(string.ascii_uppercase)
        result.append(letter)   
        if letter not in drawn_letters:
            drawn_letters[letter] = 1
        else: 
            drawn_letters[letter] += 1
        
        if drawn_letters[letter] > LETTER_POOL[letter]:
            result.remove(letter)        
    return result

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass