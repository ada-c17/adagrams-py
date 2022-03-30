import random
import copy

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

score_chart = {
    1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2 : ["D", "G"],
    3 : ["B", "C", "M", "P"],
    4 : ["F", "H", "V", "W", "Y"],
    5 : ["K"],
    8 : ["J", "X"],
    10 : ["Q", "Z"]
}



def draw_letters():
    # Overall time complexity: O(n^2) + O(4) = O(n^2)
    list_of_distribution = []


    for key, val in LETTER_POOL.items(): # O(n)
        for i in range(val): # O(n)
            list_of_distribution.append(key) # O(1)
    
    letters_in_hand = []
    for i in range(1, 11): # O(1)
        letter = random.choice(list_of_distribution) # 0(1)
        letters_in_hand.append(letter) # O(1)
        list_of_distribution.remove(letter) # O(1)
    
    return letters_in_hand

def uses_available_letters(word, letter_bank):
    # Overall time complexity: O(n^2) + O(n) + O(n) = O(n^2 + 2n) = O(n^2)

    word = word.upper() # O(n)
    found = True
    letter_bank_copy = letter_bank.copy() # O(n)
    # letter_bank_copy = copy.deepcopy(letter_bank)

    for letter in word: # O(n)
        if letter in letter_bank_copy: # O(n)
            letter_bank_copy.remove(letter) # O(1)
        else:
            found = False
    return found

# def uses_available_letters(word, letter_bank):
# Second method --> Passes tests! 
# Overall time complexity: O(n) + O(n) + O(n) = O(n)
#     word = word.upper()
#     word_dictionary = {}
#     for letter in word:
#         if letter not in word_dictionary.keys():
#             word_dictionary[letter] = 1
#         else:
#             word_dictionary[letter] += 1
    
#     letter_bank_dictionary = {}
#     for letter in letter_bank:
#         if letter not in letter_bank_dictionary.keys():
#             letter_bank_dictionary[letter] = 1
#         else:
#             letter_bank_dictionary[letter] += 1
#     # print("word_dictionary:", word_dictionary)
#     # print("letter_bank_dictionary:", letter_bank_dictionary)
#     for key in word_dictionary.keys():
#         if key not in letter_bank_dictionary.keys():
#             return False
#         elif word_dictionary[key] >= letter_bank_dictionary[key]:
#             return False
#     return True

def score_word(word):
    # Overall time complexity = O(n) + O(n) + O(n) = O(3n) = O(n)
    word = word.upper() # O(n)
    score = 0
    additional_score = [7, 8, 9, 10]


    for letter in word: # O(n)
        for key in score_chart: # O(1)
            if letter in score_chart[key]: # O(1)
                score += key

    if len(word) in additional_score: # O(n)
        score += 8
    return score

def get_highest_word_score(word_list):
    # Overall time complexity: O(n^2) + O(n)
    if len(word_list) == 0: # O(1)
        return 0
    
    result_chart = []

    for word in word_list: # O(n)
        score = score_word(word) # O(n)
        score_tuple = (word, score)
        result_chart.append(score_tuple)


    highest_word = result_chart[0]

    for item in result_chart: # O(n)
        if item[1] > highest_word[1]:
            highest_word = item
        elif item[1] == highest_word[1]:
            if (len(item[0]) == 10) and (len(highest_word[0]) != 10):
                highest_word = item

            elif (len(highest_word[0]) == 10):
                continue

            elif len(item[0]) < len(highest_word[0]):
                highest_word = item
    
    return highest_word