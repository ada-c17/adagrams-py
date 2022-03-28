from random import choice, randint
from copy import deepcopy

# create a list holding all 98 letters (letter_bank)

def draw_letters():
    pass
    user_hand = []
    copy_of_letter_bank = deepcopy(letter_bank)

    for i in range(10):
        index = randint(0, len(copy_of_letter_bank) - 1)
        letter = copy_of_letter_bank.pop(index)
        user_hand.append(letter)

    # for i in range(11):
    #     if 
    #     user_hand.append(choice(letter_pool))

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass