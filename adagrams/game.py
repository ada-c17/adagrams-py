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

# build a hand of 10 letters
def draw_letters():
    draw_pool = []
    # create a list based on LETTER_POOL
    for key, value in LETTER_POOL.items():
        draw_pool.extend([key]*value)
    # create hand with sample of random letters from draw_pool
    hand = random.sample(draw_pool, 10)
    return(hand)

def uses_available_letters(word, letter_bank):
    available_letters = letter_bank.copy()
    for letter in word:
        letter = letter.upper()
        if letter in available_letters:
            available_letters.remove(letter)
        else:
            return False
    return True

# scores word based on letter values, bonus of 8 points added for words 7-10 letters long
def score_word(word):
    score = 0
    letter_vals = {"A" : 1,
    "E" : 1,
    "I" : 1,
    "O" : 1,
    "U" : 1,
    "L" : 1,
    "N" : 1,
    "R" : 1,
    "S" : 1,
    "T" : 1,
    "D" : 2,
    "G" : 2,
    "B" : 3,
    "C" : 3,
    "M" : 3,
    "P" : 3,
    "F" : 4,
    "H" : 4,
    "V" : 4,
    "W" : 4,
    "Y" : 4,
    "K" : 5,
    "J" : 8,
    "X" : 8,
    "Q" : 10,
    "Z" : 10
    }
    for letter in word:
        letter = letter.upper()
        if letter in letter_vals:
            score += letter_vals[letter]
        else:
            continue
    if len(word) > 6 and len(word) < 11:
        score += 8
    return score

def get_highest_word_score(word_list):
    pass

