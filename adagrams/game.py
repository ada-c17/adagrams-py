import random
import copy
from webbrowser import get

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

SCORE_CHART = {
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

def draw_letters():
    '''This function returns 10 random letter tiles. Frequency of letters determined by LETTER_POOL'''
    letters = []
    letter_pool_copy = copy.deepcopy(LETTER_POOL)
    while len(letters) < 10:
        random_letter = random.choice(list(letter_pool_copy))
        if letter_pool_copy[random_letter] == 0:
            continue
        else:
            letters.append(random_letter)
            letter_pool_copy[random_letter] -= 1
    return letters

    '''PSUEDOCODE:
    1) Make deep copy of LETTER_POOL
    2) if LETTER_POOL.deepcopy value = 0; remove
        3) Generate random letter from current LETTER_POOL.deepcopy- 
        4) Find letter in LETTER_POOL.deepcopy 
        5) -1 from value
        6) append letter to letters[]
    7) Return letters[]'''

def uses_available_letters(word, letter_bank):
    '''This function checks if all letters in a word are also available in the letter_bank'''
    valid_letters = []
    word = word.upper()
    letter_bank_copy =copy.deepcopy(letter_bank)
    for letter in word:
        if letter in letter_bank_copy:
            valid_letters.append(letter)
            letter_bank_copy.remove(letter)
    if len(valid_letters) == len(word):
        letter_bank_copy = letter_bank
        return True
    else:
        letter_bank_copy = letter_bank
        return False

def score_word(word):
    '''Calculates total value of word based on letter values in SCORE_CHART'''
    word_score = 0
    word = word.upper()
    for letter in word:
        word_score += SCORE_CHART[letter]
    if len(word) in range(7,11):
        word_score += 8
    return word_score

def get_highest_word_score(word_list):
    '''Returns a tuple: ("Word", word_score) which represents the winning word.
       Tie-breakers: Words over 10 letters or shortest word wins'''
    
    scores = []
    best_words = []
    winning_word = []

    # Find highest score (int)
    for word in word_list:
        scores.append(score_word(word))
    highest_score = max(scores)

    # Create a list of all the words that equal the highest score
    for word in word_list:
        if score_word(word) == highest_score:
            best_words.append(word)

    # If only one word equals highest score
    if len(best_words) == 1:
        winning_word.append(best_words[0])
        winning_word.append(score_word(best_words[0]))
        return tuple(winning_word)
    
    # Tie-Breaker for multple words with highest score
    good_word = best_words[0]
    for word in best_words:
        if len(word) == 10:
            good_word = word
            winning_word.append(good_word)
            winning_word.append(score_word(good_word))
            return tuple(winning_word)
        elif len(word) < len(good_word):
            good_word = word
    winning_word.append(good_word)
    winning_word.append(score_word(good_word))
    return tuple(winning_word)


