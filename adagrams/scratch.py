
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
# print(uses_available_letters("ABCD", letters))

{"cat": 5, "if": 5, "doggy": 5, "cat": 5, "hamburgers": 5}

# def get_highest_word_score(word_list):
#     word_score_list = []
#     highest_word_score = 0

#     for word in word_list:
#         word_score = word_score[word]
#         word_score_list.append(word_score)
#         #len word_score_list and word_list equal size 
#     # max_scores = max(word_score_list)
#     # print(max_scores) 

#     # for i in len(word_score_list):
#         if word_score_list[i] >= highest_word_score:
#             w

#     #     if len(word_list[i]) == 10:
#     #         x, y = word_list[i], word_score[i] 
#     #         return x, y
#     #     elif:


