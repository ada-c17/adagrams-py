import random

def create_letter_pool():

    letter_pool = []

    letter_frequencies = {
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
    'Z': 1}

    for letter in letter_frequencies:

        for i in range(0, letter_frequencies[letter]):

            letter_pool.append(letter)

    return letter_pool


def draw_letters():
    
    letter_pool = create_letter_pool()

    hand = []

    while len(hand) < 10:

        num = random.randint(0, len(letter_pool)-1)
        hand.append(letter_pool[num])
        letter_pool.pop(num)

    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass