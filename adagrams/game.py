from random import shuffle
from adagrams import LETTER_POOL

def create_letter_pool():
    letter_pool = []
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
            letter_pool.append(letter)
    
    return letter_pool

# thu's suggestion for improving draw_letters():
def draw_letters():

    # it will restart every time this function is invoked
    letter_pool = create_letter_pool()
    shuffle(letter_pool)
    user_hand = letter_pool[0:10]

    return user_hand

def uses_available_letters(word, letter_bank):
    
    # make a copy of letter bank list to avoid editing original list
    copy_of_letter_bank = deepcopy(letter_bank)

    # convert all letters in word to uppercase to allow for case insensitivity
    uppercase_word = word.upper()

    # check if each letter in upper_case word is in letter_bank
    # remove the letter if identified to update occurrence frequency in list, letter_bank
    for letter in uppercase_word:
        if letter not in copy_of_letter_bank:
            return False
        else:
            copy_of_letter_bank.remove(letter)
    
    return True

def draw_letters():

    letter_pool = create_letter_pool()
    shuffle(letter_pool)
    user_hand = letter_pool[0:10]

    return user_hand

<<<<<<< HEAD
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
    
=======

def score_word(word):
<<<<<<< HEAD
    pass
=======
    score = 0

    if 7 <= len(word) <= 10:
        score += 8

    for char in word.upper():
        if char in SCORE_CHART:
            score += SCORE_CHART[char]

    return score
>>>>>>> b89d66e8969f96fcb6a428cb5fb2208269ca4077
>>>>>>> b39618dab30c8c13a3c23667ac0487c77f01b74b

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
