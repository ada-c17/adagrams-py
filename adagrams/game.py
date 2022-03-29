import random
import string
from tokenize import blank_re

letters_dict = {
    "A": 9,
    "B": 2,
    "C": 2,
    "D": 4,
    "E": 12,
    "F": 2,
    "G": 3,
    "H": 2,
    "I": 9,
    "J": 1,
    "K": 1,
    "L": 4,
    "M": 2,
    "N": 6,
    "O": 8,
    "P": 2,
    "Q": 1,
    "R": 6,
    "S": 4,
    "T": 6,
    "U": 4,
    "V": 2,
    "W": 2,
    "X": 1,
    "Y": 2,
    "Z": 1
}
def draw_letters():
    """
        output: list of 10 strings
        no parameters
        letters should be randomly drawn from a pool of letters
        letters should reflect distribution from a table
        (dictionary, pool_of_letters)
        drawn letters cannot return more than the allotted amount(?)
        once something is drawn, will probably have to subtract from the value of that letter by 1
        if the value is 0, make it no longer accessible
        possibly make list of dicts if random doesnt work?
        random.choice()?

        """
    hand_list = []
    hand_dict = letters_dict.copy()
    while len(hand_list) < 10:
        random_letter = random.choice(string.ascii_uppercase)
        for letter in hand_dict:
            if letter == random_letter:
                if hand_dict[letter] >= 1:
                    hand_list.append(letter)
                    hand_dict[letter] -= 1 
    # print(", ".join(hand_list))  
    return hand_list

def uses_available_letters(word, letter_bank):
    """
    input: word (string), letter_bank: list of drawn letters
    output: True or False
    True if every letter in word is available in letter_bank
    False if not above, or if letter in word that is not present in the letter_bank,
    or if word is longer than letter_bank
    """
    available_letters = letter_bank.copy()
    if len(word) > len(letter_bank):
        return False

    extra_letters = set(word.upper()) - set(letter_bank)
    if extra_letters:
        return False

    for letter in word.upper():
        if not letter in available_letters:
            return False
        else:
            available_letters.remove(letter)
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass