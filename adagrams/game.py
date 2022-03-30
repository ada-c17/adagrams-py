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
    # shuffle method from random module allows us to randomize the list in-place
    shuffle(letter_pool)
    # once the list is shuffled, we slice the first 10 items to use as the user's letter bank
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
    max_score = 0
    high_score_word = None

    for word in word_list:
        word_score = score_word(word)
        if word_score > max_score:
            max_score = word_score
            high_score_word = word
        elif word_score == max_score:
            word_len = len(word)
            high_score_word_len = len(high_score_word)
            # if the high score word length is not 10 AND current word length is 10 OR
            # if high score word length is not 10 AND current word length is less than high score word length
            # current word is the highest scoring word
            if high_score_word_len != 10 and (word_len == 10 or word_len < high_score_word_len):
                high_score_word = word

    return (high_score_word, max_score)