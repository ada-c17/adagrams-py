
import random

#from constants import *
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
    letter_pool = LETTER_POOL.copy()
    letters=[]
    while len(letters) < 10:
        letter = random.choice(list(letter_pool))
        letters.append(letter)
        print(len(letters), letters)
        
        letter_pool[letter]-=1
        
        if letter_pool[letter] == 0:
            letter_pool.pop(letter)
            
        print (len(letter_pool), letter_pool)   
    return letters 
    


def uses_available_letters(word, letter_bank):
    counter = 0
    upper_word = word.upper()
    for i in upper_word: 
        counter += 1
        if upper_word.count(i) == letter_bank.count(i) and counter == len(upper_word):
            return True
            
        elif upper_word.count(i) > letter_bank.count(i) and counter == len(upper_word):
            return False
 



def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass