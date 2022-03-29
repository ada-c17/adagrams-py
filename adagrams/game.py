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
    new_pool = []
    for letter, count in LETTER_POOL.items():
        new_pool.extend([letter] * count)
    
    letters = []
    already_drawn = []
    while len(letters) < 10:
        draw = random.randint(0,len(new_pool)-1)
        if draw not in already_drawn:
            letters.append(new_pool[draw])
            already_drawn.append(draw)

    return letters


def uses_available_letters(word, letter_bank):
    uppercase_word = word.upper()
    bank_copy = list(letter_bank)
    
    for char in uppercase_word:
        if char in bank_copy:
            bank_copy.remove(char)
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass