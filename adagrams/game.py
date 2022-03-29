from random import choice
from copy import copy

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
    user_hand = []
    new = copy(LETTER_POOL)

    # while len(user_hand) < 10:
    #     letter_choice = choice(list(new.keys()))
    #     if new[letter_choice] >  0:
    #         user_hand.append(letter_choice)
    #         new[letter_choice] -= 1

    available_letters = []

    for letter in LETTER_POOL:
        for num in range(0, LETTER_POOL[letter]):
            available_letters.append(letter)
    while len(user_hand) < 10:
        letter_choice = choice(available_letters)
        removed_letter = available_letters.index(letter_choice)
        user_hand.append(available_letters.pop(removed_letter))
    return user_hand

        # if new[letter_choice] >  0:
        #     user_hand.append(letter_choice)
        #     new[letter_choice] -= 1
    
    # print(len(available_letters))
    # return user_hand


def uses_available_letters(word, letter_bank):
    user_hand = copy(letter_bank)
    for letter in word.upper():
        if letter not in user_hand:
            return False
        else:
            letter_index = user_hand.index(letter)
            user_hand.pop(letter_index)
    return True

def score_word(word):
    score = 0
    points_dict = {
        "A" : 1,
        "B" : 3,
        "C" : 3,
        "D" : 2,
        "E" : 1,
        "F" : 4,
        "G" : 2,
        "H" : 4,
        "I" : 1,
        "J" : 8,
        "K" : 5,
        "L" : 1,
        "M" : 3,
        "N" : 1,
        "O" : 1,
        "P" : 3,
        "Q" : 10,
        "R" : 1,
        "S" : 1,
        "T" : 1,
        "U" : 1,
        "V" : 4,
        "W" : 4,
        "X" : 8,
        "Y" : 4,
        "Z" : 10
    } 

    for letter in word.upper():
        for key in points_dict:
            score += points_dict[key]
    if len(word) >= 7 and len(word) <= 10:
        score += 8
    return score 

def get_highest_word_score(word_list):
    pass

print(draw_letters())