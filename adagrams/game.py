from collections import Counter
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

POINT_SYSTEM = {
    'A':1,
    'B':3,
    'C':3,
    'D':2,
    'E':1,
    'F':4,
    'G':2,
    'H':4,
    'I':1,
    'J':8,
    'K':5,
    'L':1,
    'M':3,
    'N':1,
    'O':1,
    'P':3,
    'Q':10,
    'R':1,
    'S':1,
    'T':1,
    'U':1,
    'V':4,
    'W':4,
    'X':8,
    'Y':4,
    'Z':10
}



# |Letter                        | Value|
# |:----------------------------:|:----:|
# |A, E, I, O, U, L, N, R, S, T  |   1  |
# |D, G                          |   2  |
# |B, C, M, P                    |   3  |
# |F, H, V, W, Y                 |   4  |
# |K                             |   5  |
# |J, X                          |   8  |
# |Q, Z                          |   10 |

def draw_letters():
    # copy a dictionary so that we don't change the data, it's constant
    LETTER_POOL_COPY = LETTER_POOL.copy()
    letters_drawn = []
    while len(letters_drawn) < 10:
        letter_drawn = random.choice(list(LETTER_POOL_COPY)) 
        if LETTER_POOL_COPY[letter_drawn] >= 1: 
            letters_drawn.append(letter_drawn) 
            LETTER_POOL_COPY[letter_drawn] -= 1 
    return letters_drawn


def uses_available_letters(word, letter_bank):
    upper_word = word.upper()
    copy_letter_bank = letter_bank.copy()
    for char in upper_word:
        if char not in copy_letter_bank:
            return False
        else:
           copy_letter_bank.remove(char) 
    return True
           
    
       

    

def score_word(word):
    points = 0
    for char in word:
        points += POINT_SYSTEM[char.upper()]
    if len(word) >= 7 and len(word) <= 10:
        points += 8
    return points
    

def get_highest_word_score(word_list):
    pass
#     max_word = None
#     max_score = 0
#     for word in word_list:
#         word_score = score_word(word)
#         # print(max_word,max_score)
#         print(f"word_score:{word_score}")
#         print(f"word:{word}")
#         if word_score > max_score:
#             max_word = word
#             max_score = word_score
#         elif word_score == max_score:
#             print(max_word) # "MMMM"
#             print(word) # "WWW"
#             if type(max_word) != list:
#                 max_word = list(max_word)
#                 print(max_word)
#                 max_word.append(word)
#             else:
#                 max_word.append(word)
#             print(max_word) # ["MMMM","WWW"]
#     if type(max_word) == str:
#         return (max_word, max_score)
#     # print(max_word)
    
#     max_length = [] # list of each max word's lengths -> max word = all the words with max score
#     for word in max_word:
#         max_length.append(len(word))
#     max_len_index = None
#     max_len = 0
        

#     max_len_index = max_length.index(min(max_length))
#     for i in range(len(max_word)):
#         if len(max_word[i]) == 10:
#             return (max_word[i], max_score)
#     return (max_word[max_len_index],max_score)
        
# # - Returns a tuple that represents the data of a winning word and it's score.  The tuple must contain the following elements:
# #   - index 0 ([0]): a string of a word
# #   - index 1 ([1]): the score of that word
# # - In the case of tie in scores, use these tie-breaking rules:
# #     - prefer the word with the fewest letters...
# #     - ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
# #     - If the there are multiple words that are the same score and the same length, pick the first one in the supplied list