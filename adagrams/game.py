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
    #new_pool = [[a,b] for a,b in LETTER_POOL.items()]

    new_pool = []
    for a,b in LETTER_POOL.items():
        new_pool.append([a,b])

    letters = []
    while len(letters) < 10:
        draw = random.randint(0,25)
        if new_pool[draw][1] > 0:
            letters.append(new_pool[draw][0])

    return letters


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass