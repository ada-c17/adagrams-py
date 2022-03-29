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
    max_word = None
    max_score = 0
    for word in word_list:
        word_score = score_word(word)
        if word_score > max_score:
            max_word, max_score = word, word_score
        elif word_score == max_score:
            if type(max_word) != list:
                max_word = list(max_word)
            max_word.append(word)
    if type(max_word) == str:
        return (max_word, max_score)
    min_len, min_word = 100, None
    for word in word_list:
        if len(word) == 10:
            return (word,score_word(word))
        elif len(word) < min_len:
            min_word, min_len = word, len(word)
    return (min_word,score_word(min_word))
