import random
import copy
POINT_VALUES = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10
}

def draw_letters():
    pool_of_letters = ['A'] * 9 + ['B'] * 2 + ['C'] * 2 + ['D'] * 4 + ['E'] * 12 + ['F'] * 2\
    + ['G'] * 3 + ['H'] * 2 + ['I'] * 9 + ['J'] * 1 + ['K'] * 1 + ['L'] * 4 + ['M'] * 2\
    + ['N'] * 6 + ['O'] * 8 + ['P'] * 2 + ['Q'] * 1 + ['R'] * 6 + ['S'] * 4 + ['T'] * 6\
    + ['U'] * 4 + ['V'] * 2 + ['W'] * 2 + ['X'] * 1 + ['Y'] * 2 + ['Z'] * 1

    return random.sample(pool_of_letters, 10)

def uses_available_letters(word, letter_bank):
    upper_word = word.upper()
    letters_available = copy.deepcopy(letter_bank)
    for letter in upper_word:
        if letter in letters_available:
            letters_available.remove(letter)
        else:
            return False
    return True

def score_word(word):
    score = 0
    for letter in word.upper():
        score += POINT_VALUES[letter]
    if len(word) >= 7:
        score += 8
    return score

def get_highest_word_score(word_list):
    max_score = 0
    highest_word = ""
    for word in word_list:
        score = score_word(word)
        if score > max_score:
            max_score = score
            highest_word = word
        elif score == max_score and len(highest_word) != 10:
            if len(word) == 10 or len(word) < len(highest_word):
                highest_word = word
    winning_word = (highest_word, max_score)
    return winning_word


    