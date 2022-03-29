import copy
import random

LETTERS = {"A":9, "B":2, "C":2,"D":4, "E":12, "F":2, "G":3, "H":2,"I":9,"J":1,"K":1,"L":4,"M":2,"N":6, "O":8,"P":2,"Q":1,"R":6,"S":4,"T":6, "U":4, "V":2,"W":2,"X":1,"Y":2,"Z":1} 

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
    pass

def get_highest_word_score(word_list):
    pass