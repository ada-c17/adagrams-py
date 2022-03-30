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
    list = []
    for value, keys in LETTER_POOL.items():
        for k in range(keys):
            list.append(value)

    # create with rundom function list of 10 elements according list of letters with sample function
    output = sample(list, k=10)
    return output


def get_letter_count(seq):
    """Returns a dictionary that contains the frequency of each letter from a sequence"""

    frequency_dict = {}

    for char in seq:
    #     if char in frequency_dict:
    #         frequency_dict[char] += 1
    #     else:
    #         frequency_dict[char] = 1
        frequency_dict[char] = frequency_dict.get(char, 0) + 1

    return frequency_dict

def uses_available_letters(word, letter_bank):
    """Returns True if word uses only letters from letter_bank
    Returns False if word uses letters not from letter_bank"""
    word = word.upper()

    # get the counts of each character
    word_count_dict = get_letter_count(word)
    letter_bank = get_letter_count(letter_bank)

    for char, count in word_count_dict.items():
        if count > letter_bank.get(char, 0):
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
    highest_score = 0
    highest_score_word = None

    for word in word_list:
        current_score = score_word(word)

        # In case the score is strictly better
        if current_score > highest_score:
            highest_score = current_score
            highest_score_word = word
            continue


        elif current_score == highest_score:
            # if the current highest_score_word has 10 letters, continue
            if len(highest_score_word) == 10:
                continue

            # update highest_score_word to a better "option"
            if len(word) == 10 or len(word) < len(highest_score_word):
                highest_score_word = word

    return (highest_score_word, highest_score)