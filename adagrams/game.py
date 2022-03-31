import random
import string
# from random import randrange
DRAWN_LETTERS_TOTAL = 10

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

# LETTER_POOL = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
#     'B', 'B', 'C', 'C', 'D', 'D', 'D', 'D', 
#     'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 
#     'F', 'F', 'G', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I',
#     'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 
#     'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 
#     'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T',
#     'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']

SCORE_CHART = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def draw_letters():
# -------------------- SOLUTION #3--------------------
    result = []
    letter = ''

    available_pool = LETTER_POOL.copy()
    while len(result) < DRAWN_LETTERS_TOTAL:
        letter = random.choice(string.ascii_uppercase)
        if available_pool[letter] - 1 >= 0:
            result.append(letter) 
            available_pool[letter] = available_pool[letter] - 1
    return result
# -------------------- SOLUTION #1--------------------
    # randomly draw 10 letters, should match the letter pool rules
    # create a dictionary to keep track of our {current drawn letter : count}
    # update letter count in the dict
    # check if letter count is over LETTER_POOL[letter]
    # if yes, remove the letter
    # if no, do nothing
    # keep drawing until have 10 letters
    # returns an array of 10 letters
    # result = []
    # letter = ''
    # drawn_letters = {}
    # while len(result) < DRAWN_LETTERS_TOTAL:
    #     letter = random.choice(string.ascii_uppercase)
    #     result.append(letter)   
    #     if letter not in drawn_letters:
    #         drawn_letters[letter] = 1
    #     else: 
    #         drawn_letters[letter] += 1
        
    #     if drawn_letters[letter] > LETTER_POOL[letter]:
    #         result.remove(letter)  
    #     # if drawn_letters[letter] <= LETTER_POOL[letter]:
    #     #     result.append(letter)
    # return result

# -------------------- SOLUTION #2--------------------
    # result = []
    # available_letters = LETTER_POOL

    # while len(result) < DRAWN_LETTERS_TOTAL and available_letters:
    #     result.append(available_letters.pop(randrange(len(LETTER_POOL))))
    # return result

def uses_available_letters(word, letter_bank):
# -------------------- SOLUTION #2--------------------
    # getting error msg from letter bank change
    word = word.upper()
    available_letters = letter_bank[:]
    for letter in word:
        if letter in available_letters:
            available_letters.remove(letter)
        else:
            return False
    return True

# -------------------- SOLUTION #1--------------------
    # word = word.upper()
    
    # # Dictionary of letters in user's hand
    # letter_bank_dict = {}
    # for letter in letter_bank:
    #     if letter not in letter_bank_dict:
    #         letter_bank_dict[letter] = 1
    #     else:
    #         letter_bank_dict[letter] +=1

    # for letter in word:
    #     if letter not in letter_bank_dict:
    #         return False
    #     else:
    #         letter_bank_dict[letter] -= 1
    #         if letter_bank_dict[letter] < 0:
    #             return False
    # return True



def score_word(word):
    word = word.upper()
    points = 0
    for letter in word:
        points += SCORE_CHART[letter]

    if len(word) >= 7:
        points += 8

    return points

def get_highest_word_score(word_list):
# -------------------- SOLUTION #2--------------------
    highest_word = ""
    highest_score = 0

    for word in word_list:
        word_score = score_word(word)
        word_len = len(word)
        highest_word_len = len(highest_word)
        if word_score > highest_score:
            highest_word = word
            highest_score = word_score
        elif word_score == highest_score:
            if highest_word_len == 10:
                continue
            elif word_len == 10:
                highest_word = word
            elif word_len < highest_word_len:
                highest_word = word

    return (highest_word, highest_score)    

# -------------------- SOLUTION #1--------------------    
    # highest_score = 0
    # highest_word = []
    # shortest = 10
    # shortest_word = ""

    # highest_score = 0
    # for word in word_list:
    #     score = score_word(word)
    #     if score > highest_score:
    #         highest_score = score
    #         highest_word.clear() 
    #         highest_word.append(word)
    #     elif score == highest_score:
    #         highest_word.append(word)
    # if len(highest_word) == 1:
    #     return (highest_word[0], highest_score)
    # else:
    #     for word in highest_word:
    #         if len(word) == 10:
    #             return(word, score_word(word))
    #         elif len(word) < shortest:
    #             shortest = len(word)
    #             shortest_word = word 
    #     return (shortest_word, score_word(shortest_word))
    
