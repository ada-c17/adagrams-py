from random import choice, randint
from copy import deepcopy
from data import LETTER_POOL

# create a list holding all 98 letters (letter_bank)
def create_letter_pool():
    letter_pool = []
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
            letter_pool.append(letter)
    
    return letter_pool

# thu's suggestion for improving draw_letters():
# def draw_letters():

#     # it will restart every time this function is invoked
#     letter_pool = create_letter_pool()
#     shuffle(letter_pool)
#     user_hand = letter_pool[0:10]

#     return user_hand

def draw_letters():
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