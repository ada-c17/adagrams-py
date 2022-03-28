import random
from collections import Counter

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


def draw_letters():
    
    letter_list = []
    returned_letters = []
    for letter, number in LETTER_POOL.items():
        letter_list += letter * number
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
    pass

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