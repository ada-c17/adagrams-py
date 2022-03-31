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
LETTER_POINTS = {
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
    'Z': 10
}
##----------- WAVE 1 ----------- ##
def draw_letters():
    letter_pool = copy.deepcopy(LETTER_POOL)
    chosen_letters = []
    while len(chosen_letters) < 10:
        random_letter = random.choice(list(letter_pool)) 
        if letter_pool[random_letter] > 0:
            chosen_letters.append(random_letter)
            letter_pool[random_letter] -= 1
    return chosen_letters


##----------- WAVE 2 ----------- ##
def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.deepcopy(letter_bank)
    new_word = word.upper()
    for letter in new_word:
        if letter not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter)
    return True

##----------- WAVE 2 ----------- ##
def score_word(word):
    points = 0
    cased_word = word.upper()
    if len(cased_word) >= 7:
        points += 8
    for letter in cased_word:
        points += LETTER_POINTS[letter]
    
    return points


def get_highest_word_score(word_list):
    pass