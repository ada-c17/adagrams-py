
import copy
import random

# LETTERS_POOL = {"a": 1, "b": 8, "c" : 6}

# def draw_letters(LETTERS_POOL):
#     letter_list = []
#     copy_dict = copy.copy(LETTERS_POOL)
#     for i in range(10):
#         letter = random.choice(list(copy_dict))
#         copy_dict[letter] -= 1
#         letter_list.append(letter)
#         if copy_dict[letter] < 1:
#             copy_dict.pop(letter)
#         print(list(copy_dict))
#     print(letter_list)
#     return letter_list

# draw_letters(LETTERS_POOL)
# letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# def uses_available_letters(word, letter_bank):
#     list_copy = letter_bank.copy()

#     print(word)

#     #for each character in word
#     for character in word:

#         character = character.capitalize()
        
#         if character in letter_bank:
#             list_copy.remove(character)
#         else:
#             return False
#     return True

# print(uses_available_letters("ABCD", letters))

def word_score(word):
    letter_score = {
        "A": 1, 
        "E": 1, 
        "I": 1, 
        "O": 1,
        "U": 1, 
        "L": 1, 
        "N": 1, 
        "R": 1,
        "S": 1,
        "T": 1, 
        "D": 2, 
        "G": 2, 
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3, 
        "F": 4, 
        "H": 4, 
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10
    }

    extra_points= {8: [7, 8, 9, 10]}
    total = 0
    
    if len(word) in extra_points.values():
        total += 8
    for letter in word:
        total += letter_score[letter]
        #can't return a tuple here- (i.e. total, word)
    return total

print(word_score("cat"))