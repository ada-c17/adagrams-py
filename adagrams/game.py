import copy
import random

LETTERS = {"A":9, "B":2, "C":2,"D":4, "E":12, "F":2, "G":3, "H":2,"I":9,"J":1,"K":1,"L":4,"M":2,"N":6, "O":8,"P":2,"Q":1,"R":6,"S":4,"T":6, "U":4, "V":2,"W":2,"X":1,"Y":2,"Z":1} 
SCORE_CHART = {
    'A' : 1,
    'B' : 3,
    'C' : 3,
    'D' : 2,
    'E' : 1,
    'F' : 4,
    'G' : 2,
    'H' : 4, 
    'I' : 1,
    'J' : 8,
    'K' : 5,
    'L' : 1,
    'M' : 3,
    'N' : 1,
    'O' : 1,
    'P' : 3,
    'Q' : 10,
    'R' : 1,
    'S' : 1,
    'T' : 1,
    'U' : 1,
    'V' : 4,
    'W' : 4,
    'X' : 8,
    'Y' : 4,
    'Z' : 10
}

def draw_letters():
    copied_letters = copy.deepcopy(LETTERS)
    hand = []
    while len(hand)<10:
        rand_letter = random.choice(list(LETTERS.keys()))
        if copied_letters[rand_letter]>0:
            hand.append(rand_letter)
            copied_letters[rand_letter]-=1
    return hand


def uses_available_letters(word, letter_bank):
    copied_letter_bank = copy.deepcopy(letter_bank)
    if len(word) > len(copied_letter_bank):
        return False
    for letter in word.upper():
        if letter in copied_letter_bank:
            copied_letter_bank.remove(letter)
        else:
            return False
    return True

def score_word(word):
    score = 0
    if len(word) >= 7 and len(word) <= 10:
        score += 8
    for letter in word.upper():
        if letter.isalpha():
            score += SCORE_CHART[letter]
    
    return score

def get_highest_word_score(word_list):
    pass