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
    pass


def convert_word_to_upper(word):
    """
    converts all the letters of a word to upper case
    """
    upper_word = ""
    for letter in word:
        if letter.isalpha(): 
            upper_word += letter.upper()
    return upper_word

def uses_available_letters(word, letter_bank):
    upper_word = convert_word_to_upper(word)
    letter_bank_copy = copy.deepcopy(letter_bank)
    for letter in upper_word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass