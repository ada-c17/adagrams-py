from random import choice, randint, shuffle
from copy import deepcopy

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

#     for i in range(11):
#         if 
#         user_hand.append(choice(letter_pool))

# def uses_available_letters(word, letter_bank):
#     for letter in word.upper():
#         if letter not in letter_bank or word.upper().count(letter) > letter_bank.count(letter):
#             return False
#     return True


def score_word(word):
    # global variable ?
    score_chart = {
        1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2 : ["D", "G"],
        3 : ["B", "C", "M", "P"],
        4 : ["F", "H", "V", "W", "Y"],
        5 : ["K"],
        8 : ["J", "X"],
        10 : ["Q", "Z"]
    }
    points = 0
    if len(word.upper()) > 6 and len(word.upper()) < 11:
        points += 8
    for letter in word.upper():
        for key, values in score_chart.items():
            if letter in values:
                points += key
    return points
    

def get_highest_word_score(word_list):
    high_scores = []
    for word in word_list:
        word_score = score_word(word)
        high_scores.append((word, word_score))
    highest_score = max(high_scores)
    # if highest_score > 1:
    #     tied_scores = []
    #     tied_scores.append(highest_score)
    #     tied_scores.sort()
    #     for tiebreaker in tied_scores:
    #         if highest_score[1] in tied_scores[0] or len(highest_score[0]) == 10:
    #             highest_score = tiebreaker
    #             return highest_score
    #         else:
    #             return tied_scores[0]
    return highest_score
