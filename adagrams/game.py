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
    
    letter_list = []
    returned_letters = []
    for letter, number in LETTER_POOL.items():
        letter_list += letter * number[0]
    for i in range(10):
        current_letter = letter_list[random.randint(0, len(letter_list) - 1)]
        returned_letters.append(current_letter)
        letter_list.remove(current_letter)

    return returned_letters
    pass

def uses_available_letters(word, letter_bank):
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
    score = 0
    for letter in word:
        score += LETTER_POOL[letter.upper()][1]
    if len(word) > 6:
        score += 8
    return score


def get_highest_word_score(word_list):
    pass


# letters = {
#     "a" : 5,
#     "b" : 4
# }
# letter_list = []
# for letter, number in letters.items():
#     letter_list += letter * number
# print(letter_list)