import random

def get_letter_frequency(letter_dict, letter):
    """
    Takes in a dictionary (letter_dict), and string (letter). 
    Returns a dictionary where keys are the string, and values are the count.
    """
    if letter not in letter_dict:
        letter_dict[letter] = 1
    elif letter in letter_dict:
        letter_dict[letter] += 1
    
    return letter_dict


def draw_letters():
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

    hand = []
    letters_count = {}
    letters = list(LETTER_POOL.keys())

    while len(hand) < 10:
        random_letter = random.choice(letters)
        letters_count = get_letter_frequency(letters_count, random_letter)
        letter_limit = LETTER_POOL[random_letter]

        if letters_count[random_letter] > letter_limit:
            continue

        hand.append(random_letter)
    
    return hand   

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass