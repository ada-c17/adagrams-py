import random
import string
DRAWN_LETTERS_TOTAL = 10

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
    result = []
    letter = ''

    available_pool = LETTER_POOL.copy()
    while len(result) < DRAWN_LETTERS_TOTAL:
        letter = random.choice(string.ascii_uppercase)
        if available_pool[letter] - 1 >= 0:
            result.append(letter) 
            available_pool[letter] = available_pool[letter] - 1
    return result

def uses_available_letters(word, letter_bank):
    word = word.upper()
    available_letters = letter_bank[:]
    for letter in word:
        if letter in available_letters:
            available_letters.remove(letter)
        else:
            return False
    return True

def score_word(word):
    word = word.upper()
    points = 0
    for letter in word:
        points += SCORE_CHART[letter]

    if len(word) >= 7:
        points += 8

    return points

def get_highest_word_score(word_list):
    highest_word = ""
    highest_score = 0

    for word in word_list:
        word_score = score_word(word)
        word_len = len(word)
        highest_word_len = len(highest_word)
        if word_score > highest_score:
            highest_word = word
            highest_score = word_score
        elif word_score == highest_score:
            if highest_word_len == 10:
                continue
            elif word_len == 10:
                highest_word = word
            elif word_len < highest_word_len:
                highest_word = word

    return (highest_word, highest_score)   