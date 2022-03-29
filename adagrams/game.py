from random import shuffle
from collections import Counter

# get a random num between 0-25
# use random number to locate letter from letter pool - where the letter corresponds w/index
# add letter to hand and update letter pool minus letter from letter pool
# repeat process 10x (or until letter hand has 10)- while
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

    letters = []

    letter_bag = list(Counter(LETTER_POOL).elements())
    shuffle(letter_bag)

    for letter in range(10):
        letters.append(letter_bag.pop())
    return letters


def uses_available_letters(word, letter_bank):

    letter_bank_copy = letter_bank.copy()
    for letter in word.upper():
        if letter not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter)
    return True



def score_word(word):
    score = 0
    one_point = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    two_points = ['D', 'G']
    three_points = ['B', 'C', 'M', 'P']
    four_points = ['F', 'H', 'V', 'W', 'Y']
    five_points = ['K']
    eight_points = ['J', 'X']
    ten_points = ['Q', 'Z']
    for letter in word.upper():
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
    if len(word) >= 7:
        score += 8
    return score 


def get_highest_word_score(word_list):
    score_list = {}
    for word in word_list:
        word_score = score_word(word)
        score_list[word] = word_score

    highest_score = max(score_list, key=score_list.get)
    

    print(highest_score)






#     letter_pool = [
#         {'A': 9}, 
#     {'B': 2}, 
#     {'C': 2}, 
#     {'D': 4}, 
#     {'E': 12}, 
#     {'F': 2}, 
#     {'G': 3}, 
#     {'H': 2}, 
#     {'I': 9}, 
#     {'J': 1}, 
#     {'K': 1}, 
#     {'L': 4}, 
#     {'M': 2}, 
#     {'N': 6}, 
#     {'O': 8}, 
#     {'P': 2}, 
#     {'Q': 1}, 
#     {'R': 6}, 
#     {'S': 4}, 
#     {'T': 6}, 
#     {'U': 4}, 
#     {'V': 2}, 
#     {'W': 2}, 
#     {'X': 1}, 
#     {'Y': 2}, 
#     {'Z': 1}
# ]

# LETTER = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # COUNT = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]