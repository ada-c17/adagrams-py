#from tests.test_wave_01 import LETTER_POOL
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

SCORE_DICT = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"], 
    3: ["B", "C", "M", "P"], 
    4: ["F", "H", "V", "W", "Y"], 
    5: ["K"], 
    8: ["J", "X"], 
    10: ["Q", "Z"]
    }

def draw_letters():
    random_letter = []
    is_valid = True
    while is_valid:
        letter = random.choice(list(LETTER_POOL))
        if random_letter.count(letter) < LETTER_POOL[letter]:
            random_letter.append(str(letter))
        if len(random_letter) == 10:
            is_valid = False
    return random_letter

    

def uses_available_letters(word, letter_bank):
    cap_letter = word.upper()
    for letter in cap_letter:
        if cap_letter.count(letter) <= letter_bank.count(letter):
            if letter in letter_bank:
                continue
        else:
            return False
    return True

def score_word(word):
    cap_letter = word.upper()
    score = 0
    for letter in cap_letter:
        for key, value in SCORE_DICT.items():
            if letter in value:
                score += key
    if len(word) >= 7:
        score += 8
            
    return score

def get_highest_word_score(word_list):

    highest_score = 0
    highest_word = ()
    for word in word_list:
        if score_word(word) == highest_score:
            if len(highest_word) == 10:
                continue
            elif len(word) == 10 or len(word) < len(highest_word):
                highest_word = word
        else:
            if score_word(word) > highest_score:
                highest_score = score_word(word)
                highest_word = word 

    return (highest_word, highest_score) 

    

    



    


