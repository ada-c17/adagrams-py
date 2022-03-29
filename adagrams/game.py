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


#isolate the keys into thier own list
#isolate the values into their own list
#mulitply the two lists together
#import random
# use random sampling off the new list to choose the 10 letters
# return 10 letters


def draw_letters():
    letters = list(LETTER_POOL.keys())
    
    letter_quantity = list(LETTER_POOL.values())

    pool_strings = []

    pool = []

    for i in range(len(letters)):
        pool_strings.append(letters[i] * letter_quantity[i])

    for string in pool_strings:    
        for letter in string:
            pool.append(letter)

    letter_bank = list(random.sample(pool, 10))
    return letter_bank
            

def uses_available_letters(word, letter_bank):
    if isinstance(word, str) and len(word) <= 10:
        word_up = word.upper()
        bank_dict = {}
        word_dict = {}

        for letter in letter_bank:
            if letter in bank_dict:
                bank_dict[letter] += 1
            else:
                bank_dict[letter] = 1

        for letter in word_up:
            if letter in word_dict:
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1  
        
        for letter in word_up:
            if word_dict[letter] <=  bank_dict[letter]:
                for letter in word_up:
                    if letter not in letter_bank:
                        return False
                return True
            return False
    return False


#List1 all of the letters for each point
# for letter in word if in list



def score_word(word):
    score = 0

    one_point = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    two_points = ["D", "G"]
    three_points = ["B", "C", "M", "P"]
    four_points = ["F", "H", "V", "W", "Y"]
    five_points = ["K"]
    eight_points = ["J", "X"]
    ten_points = ["Q", "Z"]
    long_word_bonus = [7, 8, 9, 10]

    word_up = word.upper()
    
    if len(word_up) in long_word_bonus:
        score += 8

    for letter in word_up:
        if letter in one_point:
            score += 1
        elif letter in two_points:
            score += 2
        elif letter in three_points:
            score += 3
        elif letter in four_points:
            score += 4
        elif letter in five_points:
            score += 5
        elif letter in eight_points:
            score += 8
        elif letter in ten_points:
            score += 10

    return score

def get_highest_word_score(word_list):
    pass