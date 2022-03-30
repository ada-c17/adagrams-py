import random
import copy
from re import L
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
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K"): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10
}

def draw_letters():

    letter_pool_copy = copy.deepcopy(LETTER_POOL)   # shallow copy should work in this case? it's faster than deep copy, deep copy complexity is varied
    drawn_letters = []                              

    for i in range(10):
        letter = random.choice(list(letter_pool_copy.keys()))
        if letter_pool_copy[letter] == 1:
            del letter_pool_copy[letter]       
        else:
            letter_pool_copy[letter] -= 1
        drawn_letters.append(letter)
    return drawn_letters

def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.deepcopy(letter_bank)   # 2nd thought: we might use a dictionary to store the letter data? key:value --> letter:freq
    for char in word:                               # checking an item in dictionary is O(1), checking an item in list is O(n)
        char = char.capitalize()                    # the good thing is, we only have 10 letters so the space complextiy will be O(1) no matter what
        if char not in letter_bank_copy:        
            return False            # Switch the order of the return and remove
        letter_bank_copy.remove(char)               # list.remove method time complexity is O(n), update the value in dict is O(1) in the most cases
    return True

def score_word(word):
    score = 0
    word = word.upper()
    for letter in word:                            # still thinking might use update the SCORE_CHART ----> single_letter:score
        for char, value in SCORE_CHART.items():    # it reduce the time complexity from n^2 to n, and it won't take too many space because there're
            if letter in char:                     # 26 letters at the most, how do you think :)
                score += value

    if len(word) >= 7:
        score += 8

    return score


def get_highest_word_score(word_list):

    words_score = {}
    words_max_value = []

    for word in word_list:                          # line 85 to 88 can be combined. Within one iteration, we can get the score and max_value. 
        words_score[word] = score_word(word)        # and we can get length as well. but I couldn't think about an effiency data structure to store
                                                    # that many information at once without using nested array :(
    max_value = max(words_score.values())

    for word, score in words_score.items():
        if score == max_value:
            words_max_value.append(word)

    if len(words_max_value) > 1:
        words_max_value = sorted(words_max_value, key=len)
        for word in words_max_value:
            if len(word) == 10:
                return word, max_value    
    return words_max_value[0], max_value


def wave4(word_list):
    word_list = sorted(word_list, key = len)
    max_value = 0
    words_max_value = []
    words_score = {}

    for word in word_list:
        cur_score = score_word(word)
        words_score[word] = cur_score
        max_value = max(max_value, cur_score)
    
    for i in range(len(words_score)-1, -1, -1):
        cur_word = words_score[i]
        if len(cur_word) != 10 or i == 0:
            return words_score[0], max_value
        elif len(words_score[i-1]) != 10:
            return words_score[i], max_value


print(wave4(["XXX", "XXXX", "XX", "X"]))
