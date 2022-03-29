import random
import copy

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

score_chart = {
    1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2 : ["D", "G"],
    3 : ["B", "C", "M", "P"],
    4 : ["F", "H", "V", "W", "Y"],
    5 : ["K"],
    8 : ["J", "X"],
    10 : ["Q", "Z"]
}



def draw_letters():
    list_of_distribution = []


    for key, val in LETTER_POOL.items():
        for i in range(val):
            list_of_distribution.append(key)
    
    letters_in_hand = []
    for i in range(1, 11):
        letter = random.choice(list_of_distribution)
        letters_in_hand.append(letter)
        list_of_distribution.remove(letter)
    
    return letters_in_hand

def uses_available_letters(word, letter_bank):
    word = word.upper()
    found = True
    letter_bank_copy = copy.deepcopy(letter_bank)
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            found = False
    return found

# def uses_available_letters(word, letter_bank):
#     word = word.upper()
#     word_dictionary = {}
#     for letter in word:
#         if letter not in word_dictionary.keys():
#             word_dictionary[letter] = 1
#         else:
#             word_dictionary[letter] += 1
    
#     letter_bank_dictionary = {}
#     for letter in letter_bank:
#         if letter not in letter_bank_dictionary.keys():
#             letter_bank_dictionary[letter] = 1
#         else:
#             letter_bank_dictionary[letter] += 1
#     # print("word_dictionary:", word_dictionary)
#     # print("letter_bank_dictionary:", letter_bank_dictionary)
#     for key in word_dictionary.keys():
#         if key not in letter_bank_dictionary.keys():
#             return False
#         elif word_dictionary[key] >= letter_bank_dictionary[key]:
#             return False
#     return True

def score_word(word):
    word = word.upper()
    score = 0
    additional_score = [7, 8, 9, 10]


    for letter in word:
        for key in score_chart:
            if letter in score_chart[key]:
                score += key

    if len(word) in additional_score:
        score += 8
    return score

def get_highest_word_score(word_list):
    pass