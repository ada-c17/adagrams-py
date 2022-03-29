
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

letter_point ={
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K"): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10
}

import random


def draw_letters():
    """Drawing 10 letters from a pool of letter and return a list of that letters"""
    # a list to store all letters from a pool of letter
    list_letter = []
    # loop over LETTER_POOL to get key and value
    # key will be the letter adding to list and 
    # value is number of times that the letter will be adding
    for letter, count in LETTER_POOL.items():
        # adding letter into list depend on value of count 
        for i in range(count):
            list_letter.append(letter)
    # create a list that randomly draw 10 letters from list_letter 
    letter_draw = random.sample(list_letter, k=10)
    
    return letter_draw


def uses_available_letters(word, letter_bank):
    """
    Checking each letter of word:
        - return False if it is not in letter_bank
        - return True if it is in letter_banks
    """
    # create a new list which same as letter_bank, so it doen't effect to original when editing
    letter_bank_copy = letter_bank.copy()
    # loop over word to get each character
    for char in word.upper():
        # return False if the character of word not in the new created list
        if char not in letter_bank_copy:
            return False
        # otherwise removing each character of word from letter_bank_copy when it is in there
        # return True after removing all characters of word that is in letter_bank_copy
        else: 
            letter_bank_copy.remove(char)
    return True


def score_word(word):
    """
    Sum score of each character of input
        - return 0 if input is empty or number, otherwise:
        - sum point if the character of input is uppercase or lowercase and it is in table of point value
        - if input has special character then point value is 0
        - return total score at the end
    """
    # create a variable to sum score for all valid input
    total_score = 0
    # return 0 when input is integer or float
    if isinstance(word, int) or isinstance(word, float):
        return 0
    
    # return 0 when input is empty
    elif len(word) == 0:
        return 0
    # otherwise, sum score when it matches below conditon
    else:
        # loop over char_point dictionary to get key and value for comparing
        for letter, point in letter_point.items():
            # loop over the word to get each character and check whether is it in the key of char_point
            for char in word:
                # get point value from char_point dictionary to sum if character of word is string and it is in tuple key of dictionary
                if isinstance(char, str) and char.upper() in letter:
                    total_score += point
                # otherwise, the point value of special character will assign 0 then sum
                else:
                    total_score += 0
        # if length of word is from 7 to 10, add additional 8 point
        if len(word) > 6 and len(word) < 11:
            total_score += 8
    return total_score


def get_highest_word_score(word_list):
    word_dict = {}
    max_score = 0
    best_word = []
    for word in word_list:
        score = score_word(word)
        word_dict[word] = score
        if score >= max_score:
            max_score = score
    for key, value in word_dict.items():
        if value == max_score:
            best_word.append(key)

    if len(best_word) == 1:
        best_word.append(max_score)
        return tuple(best_word)
    else:
        max_len = len(best_word[0])
        win_word = ""
        for i in range(len(best_word) - 1):              
            if len(best_word[i+1]) == max_len:
                best_word.remove(best_word[i+1])
            elif len(best_word[i]) == 10:
                win_word = best_word[i]
                best_word.clear()
                best_word.append(win_word)
            else: 
                if len(best_word[i+1]) != 10 and len(best_word[i+1]) > max_len:
                    best_word.remove(best_word[i+1])
                else:
                    best_word.remove(best_word[i])
                    
    best_word.append(max_score)
    return tuple(best_word)