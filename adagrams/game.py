'''
A program to set up and run the Adagrams Game.
The goal of the game is to create words drawn from a 
limitted letter pool. Each word is scored based off 
of which letters were used and based off of length.

Used the random module in order to selet a random array
of letters from the LETTER_POOL and add the to the
letter bank.

Used Counter subclass from the collections module 
to collect the information on the remaining amount 
of each letter in the letter bank.

'''


import random
from collections import Counter

LETTER_POOL = {
    'A': [9, 1], 
    'B': [2, 3], 
    'C': [2, 3], 
    'D': [4, 2], 
    'E': [12, 1], 
    'F': [2, 4], 
    'G': [3, 2], 
    'H': [2, 4], 
    'I': [9, 1],
    'J': [1, 8],
    'K': [1, 5],
    'L': [4, 1],
    'M': [2, 3],
    'N': [6, 1], 
    'O': [8, 1],
    'P': [2, 3],
    'Q': [1, 10], 
    'R': [6, 1],
    'S': [4, 1],
    'T': [6, 1], 
    'U': [4, 1], 
    'V': [2, 4], 
    'W': [2, 4], 
    'X': [1, 8], 
    'Y': [2, 4],
    'Z': [1, 10]
}


def draw_letters():
    """
    Creates a list of letters based on frequency table, then randomly selects 10 letters

        Parameters:
                None

        Returns:
                returned_letters (list): list of 10 randomly chosen letters
    """
    letter_list = []
    returned_letters = []
    for letter, number in LETTER_POOL.items():
        letter_list += letter * number[0]
    for i in range(10):
        current_letter = letter_list[random.randint(0, len(letter_list) - 1)]
        returned_letters.append(current_letter)
        letter_list.remove(current_letter)

    return returned_letters
    

def uses_available_letters(word, letter_bank):
    """
    Checks if the provided word utilizes letters only found in letter bank

        Parameters:
                word (str): the played word
                letter_bank (list): bank of randomly assigned letters

        Returns:
                boolean value based on word validity
    """
    letter_dict = Counter(letter_bank)

    for letter in word.upper():
        try:
            if letter in letter_dict.keys() and letter_dict[letter] > 0:
                letter_dict[letter] -= 1
            else:
                return False
        except KeyError:
            return False
    
    return True

def score_word(word):
    ''' 
    Scores the word based on the points in the 
    LETTER_POOL dictionary and the additional rule
    if the word is longer than 6 characters then it
    will add 8 to the total score.

        Parameters: 
                word(str): the word to be scored
        Returns: 
                The total score of the word. (int)
    '''
    score = 0
    for letter in word:
        score += LETTER_POOL[letter.upper()][1]
    if len(word) > 6:
        score += 8
    return score


def get_highest_word_score(word_list):

    '''
    Calculates the highest score in a list of words.

    Analyzes high scores to check for a tie. 
    Follows game rules for tie breaker:

    Ties are judged based off of letter count:

    If Their is a 12 letter word present, returns the
    first 12 letter word that appears in the list.

    For cases without a 12 letter word, returns the 
    shortest word in the list.

    If the shortest words are the same length, return
    the one that appears first in the original list.

        Parameters:
                List of words to be scored.
        
        Returns: 
                A tuple of the highest scoring word followed
                by its point value.

    '''

    scores = []
    lowest = ()

    for word in word_list:
        current_word_score = score_word(word)
        if not scores: 
            scores.append((word, current_word_score))
        elif current_word_score > scores[0][1]:
            scores = [(word, current_word_score)]
        elif current_word_score == scores[0][1]:
            scores.append((word, current_word_score))

    if len(scores) == 1:
        return scores[0]

    for word, top_score in scores:
        word_length = len(word)
        if word_length == 10:
            return word, top_score
        elif not lowest:
            lowest = (word, top_score, word_length)
        elif word_length < lowest[2]:
            lowest = (word, top_score, word_length)

    return lowest[0], lowest[1]
