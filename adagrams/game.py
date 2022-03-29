from random import shuffle
from collections import Counter

# get a random num between 0-25
# use random number to locate letter from letter pool - where the letter corresponds w/index
# add letter to hand and update letter pool minus letter from letter pool
# repeat process 10x (or until letter hand has 10)- while
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


def draw_letters():
    letter_pool = {
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
    letters = []

    letter_bag = list(Counter(letter_pool).elements())
    shuffle(letter_bag)

    for letter in range(10):
        letters.append(letter_bag.pop())
    return letters


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass


#     letter_pool = [
#         {'A': 9}, 
#     {'B': 2}, 
#     {'C': 2}, 
#     {'D': 4}, 
#     {'E': 12}, 
#     {'F': 2}, 
#     {'G': 3}, 
#     {'H': 2}, 
#     {'I': 9}, 
#     {'J': 1}, 
#     {'K': 1}, 
#     {'L': 4}, 
#     {'M': 2}, 
#     {'N': 6}, 
#     {'O': 8}, 
#     {'P': 2}, 
#     {'Q': 1}, 
#     {'R': 6}, 
#     {'S': 4}, 
#     {'T': 6}, 
#     {'U': 4}, 
#     {'V': 2}, 
#     {'W': 2}, 
#     {'X': 1}, 
#     {'Y': 2}, 
#     {'Z': 1}
# ]

# LETTER = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # COUNT = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]