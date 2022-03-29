
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





# def get_highest_word_score(word_list):
#     highest_word = ""
#     highest_score = 0

#     for word in word_list:
#         score = score_word(word)

#         if score > highest_score:
#             highest_score = score
#             highest_word = word
#         elif score == highest_score:
#             if len(word) == 10 and len(highest_word) != 10:
#                 highest_word == word
#             elif len(word) < len(highest_word):
#                 highest_word = word
#             else:
#                 continue
        
#     return highest_word, highest_score

# def score_word(word):
#     if not word:
#         return 0

#     score = 0

#     for letter in word:
#         letter = letter.capitalize()
#         if letter.isalpha():
#             score += LETTER_SCORES[letter]
    
#     if len(word) >= 7:
#         score += 8
    
#     return score