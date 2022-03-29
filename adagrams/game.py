def draw_letters():
    pass

import copy
def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.deepcopy(letter_bank)
    for letter in word:
        letter = letter.upper()
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass