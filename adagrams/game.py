from random import sample

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



SCORE_DICT = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1,
    'P': 3,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'W': 4,
    'X': 8,
    'Y': 4,
    'Z': 10
}


def draw_letters():
    # create the list of letters from dictionary according quantity
    letters = []
    for letter, frequency in LETTER_POOL.items():
        for k in range(frequency):
            letters.append(letter)

    # create with rundom function list of 10 elements according list of letters with sample function
    output = sample(letters, k=10)
    return output

# create a helper function
def get_letter_count(sequence):
    """Returns a dictionary that contains the frequency of each letter from a sequence"""

    frequency_dict = {}

    for character in sequence:
        frequency_dict[character] = frequency_dict.get(character, 0) + 1

    return frequency_dict

def uses_available_letters(word, letter_bank):
    """Returns True if word uses only letters from letter_bank
    Returns False if word uses letters not from letter_bank"""
    word = word.upper()

    # get the counts of each character
    word_count_dict = get_letter_count(word)
    letter_bank = get_letter_count(letter_bank)

    for character, count in word_count_dict.items():
        if count > letter_bank.get(character, 0):
            return False

    return True

def score_word(word):
    # check empty word
    if len(word) == 0:
        return 0
    # make letter in upper case
    word = word.upper()
    
    # create score according dictionary values
    score = 0
    for letter in word:
        if letter in SCORE_DICT:
            score += SCORE_DICT[letter]
    
    # if the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
    if len(word) in [7,8,9,10]:
        score += 8
    return score

def get_highest_word_score(word_list):
    pass