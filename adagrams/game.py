from os import truncate
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

LETTER_SCORES = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}

def make_letter_pool_list():
    letter_pool_list = []
    
    for letter, count in LETTER_POOL.items():
        letter_pool_list += [letter]*count
    return letter_pool_list

def draw_letters():
    letter_bank = random.sample(make_letter_pool_list(), 10)
    return letter_bank




def uses_available_letters(word, letter_bank):
    # compare the letters in word with the letters in letter_bank
    #for letter in word if in letter_bank
    # return true if all letters in word are in letter_bank
    # else return fals
    temp_letter_bank = list(letter_bank)
    for letter in word.upper():
        if letter in temp_letter_bank:
            temp_letter_bank.remove(letter)
        else:
            return False
    return True
    # for letter in letter_bank:
    #     if letter in word:
    #         continue
    #     else:
    #         return False
    #     return True

    

def score_word(word):
    if len(word) >= 7:
        word_score = 8
    else:
        word_score = 0
    for letter_to_score in word.upper():
        for score, letter_list in LETTER_SCORES.items():
            if letter_to_score in letter_list:
                word_score += score
    return word_score



def get_highest_word_score(word_list):
    highest_word = ("word", 0)
    for word in word_list:
        score = score_word(word)
        if score > highest_word[1]:
            highest_word = (word, score)
    for word in word_list:
        score = score_word(word)
        if score == highest_word[1]:
            if len(word) == len(highest_word[0]) and word != highest_word[0]:
            # without the second conditional, the above if statement will
            # break when the iterator reaches the same word. we want
            # to break the tie by returning the earlier word in the list
            # only when we compare different words, hence the != conditional.
                break
            elif len(word) == 10:
                highest_word = (word, score)
            elif len(highest_word[0]) == 10:
                break
            elif len(word) < len(highest_word[0]):
                highest_word = (word, score)
                
    return highest_word
