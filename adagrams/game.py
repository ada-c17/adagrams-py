# from tests.test_wave_01 import LETTER_POOL
import random
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

SCORE_CHART = {
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T") : 1,
    ("D", "G") : 2,
    ("B", "C", "M", "P") : 3,
    ("F", "H", "V", "W", "Y") : 4,
    ("K") : 5,
    ("J","X") : 8,
    ("Q","Z") : 10,
}


def draw_letters():
    '''
    Creates a new randomized list of letters from LETTER_POOL.
    Returns: A randomized list of ten letters.
    '''

    letters = [letter for letter, letter_frequency in LETTER_POOL.items() for number in range(letter_frequency)]

    random.shuffle(letters)

    return letters[:10]

def uses_available_letters(word, letter_bank):
    '''
    Checks that each letter is listed in the dictionary as >= 
    as used in the word.

    Parameters: string, dict (word and letter frequency)
    Returns a Boolean value representing the validity of the input.
    '''

    word_uppercase = word.upper()
    
    for letter in word_uppercase:
        if letter not in letter_bank or (word_uppercase.count(letter) > letter_bank.count(letter)):
            return False
        
    return True


def score_word(word):
    '''
    Score is given to each letter based on the score chart dictionary.
    If the word is between 7 and 10, add 8 points to score.

    Parameters: A string of the word.

    Returns the score of the word.
    '''
    score = 0
    word_uppercase = word.upper()
    if len(word_uppercase) >= 7 and len(word_uppercase) <= 10: 
        score += 8
    for letter in word_uppercase:
        for letter_freq in SCORE_CHART:
            if letter in letter_freq:
                score += SCORE_CHART[letter_freq]
    return score


def get_index_tie_break(word_list):
    '''
    Checks if the length of the word is 10, then checks for the first word with the fewest letters
    Otherwise, returns the first word.

    Parameter: List of highest scoring, tied words.

    Return the index of the winning word.
    '''
    highest_index = 0
    for i in range(len(word_list)):
        if len(word_list[i]) == 10: 
            return i
        elif len(word_list[i]) < len(word_list[highest_index]):
            highest_index = i
    return highest_index


def get_highest_word_score(word_list):
    '''
    Calculate high score for each word using score_word and calculate the winner if there is a 
    tie using get_index_tie_break(). 

    Parameter: A list of words.

    Returns a tuple of the highest scoring word and its high score.
    '''
    highest_scoring_words = []
    high_score = 0
    high_score_index = 0
    for word in word_list: 
        score = score_word(word)
        if score > high_score:
            highest_scoring_words = [word]
            high_score = score
        elif score == high_score:
            highest_scoring_words.append(word)
    if len(highest_scoring_words) > 1:
        high_score_index = get_index_tie_break(highest_scoring_words)
    return highest_scoring_words[high_score_index], high_score
