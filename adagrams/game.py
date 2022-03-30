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
    1) import the random module and make LETTER_POOL a global variable
    2) how should we iterate through the LETTER_POOL?
        a) make each letter-value pair a dictionary as an element in a tuple/list?
        B) put values of the letters in a list (Like nine A elements, two B elements, etc.)
    3) use a method from the random module to shuffle the list
    4) return the first 10 elements in the shuffled list
    '''
    # letters = []
    # for letter, number in LETTER_POOL.items():
    #     for i in range(number):
    #         letters.append(letter)

    letters = [letter for letter, letter_frequency in LETTER_POOL.items() for number in range(letter_frequency)]

    random.shuffle(letters)

    return letters[:10]

def uses_available_letters(word, letter_bank):
    '''
    1) Iterate over each letter in word
    2) If the letter is not in letter_bank or the frequency of 
    the letter in word is greater than the frequency of the 
    letter in letter_bank...
    3) is_valid becomes False
    4) Break the loop
    5) return is_valid
    6) For the last test: the letters in word can be lower or upper case.
    7) The letter can only be used as frequent as it is in letter_bank.
    '''
    # letter_bank_uppercase = list(("".join(letter_bank)).upper())
    # letter_bank_lowercase = list(("".join(letter_bank)).lower())
    # letter_bank_diff_cases = tuple(letter_bank_uppercase + letter_bank_lowercase)
    # print(letter_bank_diff_cases)

    word_uppercase = word.upper()
    
    is_valid = True
    for letter in word_uppercase:
        if letter not in letter_bank or (word_uppercase.count(letter) > letter_bank.count(letter)):
            is_valid = False
            break
        
    return is_valid


def score_word(word):
    '''
    Create a SCORE_CHART dictionary with letters: point values where letters is a tuple of letters and values are integers.
    Initialize score integer.
    If length of word between 7 and 10, add 8 to score.
    iterate over string
        iterate over the dictionary to get the point value
            add to score
    return score
    '''
    score = 0
    word_uppercase = word.upper()
    if len(word_uppercase) >= 7 and len(word_uppercase) <= 10: 
        score += 8
    for letter in word_uppercase:
        for k in SCORE_CHART:
            if letter in k:
                score += SCORE_CHART[k]
    return score


def get_tie_break(word_list):
    pass


def get_highest_word_score(word_list):
    '''
    ties: 
        10 letters > fewest letters > first word 
    1) initialize an empty list variable for the highested_scoring_words
    2) initialize highested_score variable
    3) iterate over the word in word_list
    4) call score_word on each of the words
    5) store all of the highested scoring words into call score_word on each of the words
    6) if score > highested_score, overwrite the list with highest_   score_words, overwrite the highest_score with the score
    7) elif score == highested_score, add it to the highested_scoring_words
    8) if length of highested_scoring_words > 1, tie break function?
    9) Tie-break should return the index of the highested scoring word
    10) the a tuple of highest_scoring_words the first element and
    the score
    '''

    pass
