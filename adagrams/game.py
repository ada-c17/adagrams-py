import random
# Imported random library to utilize random.choice() method
# choice() method returns a randomly selected element from a specified sequencee
# Used choice() to randomly select a letter from the letter pool

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


def get_letter_frequency(letter_dict, letter):
    """
    Takes in a dictionary (letter_dict), and string (letter). 
    Returns a dictionary where keys are the letter, and values are the count.
    """
    if letter not in letter_dict:
        letter_dict[letter] = 1
    elif letter in letter_dict:
        letter_dict[letter] += 1
    
    return letter_dict


def draw_letters():
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
    points = 0
    word_all_caps = word.upper()

    if len(word) >= 7:
        points += 8

    for letter in word_all_caps:
        points += LETTER_POINTS[letter]

    return points

def get_highest_word_score(word_list):
    pass