from random import shuffle
from adagrams import LETTER_POOL, SCORE_CHART
from copy import deepcopy

def create_letter_pool():
    letter_pool = []
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
            letter_pool.append(letter)
    
    return letter_pool


def draw_letters():

    letter_pool = create_letter_pool()
    shuffle(letter_pool)
    letter_bank = letter_pool[0:10]

    return letter_bank


def uses_available_letters(word, letter_bank):
    
    # make a copy of letter bank list to avoid editing original list
    copy_of_letter_bank = deepcopy(letter_bank)

    # check if each letter in upper_case word is in letter_bank
    # remove the letter if identified to update occurrence frequency in list, letter_bank
    for letter in word.upper():
        if letter not in copy_of_letter_bank:
            return False
        else:
            copy_of_letter_bank.remove(letter)
    
    return True


def score_word(word):

    score = 0

    if 7 <= len(word) <= 10:
        score += 8

    for char in word.upper():
        if char in SCORE_CHART:
            score += SCORE_CHART[char]

    return score


def get_highest_word_score(word_list):
    high_scores = [] # [("XXXX", 10), ("XX", 10),]
    highest_score = 0

    for word in word_list:
        word_score = score_word(word)
        if word_score >= highest_score:
            highest_score = word_score
            high_scores.append((word, word_score))

    # max function is returning the first instance tuple with the highest score from high scores list
    highest_tuple = max(high_scores)
    # we are removing the tuple with the highest score from high scores list to check for other instances
    high_scores.remove(highest_score)

    # for score in high_scores:
    #     if score == highest_score:
    #         if len() == 10:

    return highest_score
