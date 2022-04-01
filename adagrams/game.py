import random
""" Random library is used in draw letter function to randomly draw 10 letters"""

LETTER_QUANTITY_DICT = {
    'A' : 9, 'N' : 6 ,
    'B' : 2, 'O' : 8, 
    'C' : 2, 'P' : 2, 
    'D' : 4, 'Q' : 1, 
    'E' : 12,'R' : 6,
    'F' : 2, 'S' : 4, 
    'G' : 3, 'T' : 6,
    'H' : 2, 'U' : 4,
    'I' : 9, 'V' : 2, 
    'J' : 1, 'W' : 2,
    'K' : 1, 'X' : 1, 
    'L' : 4, 'Y' : 2,
    'M' : 2, 'Z' : 1}

def draw_letters():
    letter_list = []

    for letter, quantity in LETTER_QUANTITY_DICT.items():
        counter = 0
        while counter < quantity:
            letter_list.append(letter)
            counter += 1
    
    letter_bank = random.sample(letter_list, 10)

    return letter_bank


def uses_available_letters(word, letter_bank):
    if not check_letters_intersecting(word,letter_bank):
        return False
    elif check_letters_intersecting(word,letter_bank):
        for letter in word.upper(): 
            if word.count(letter) <= letter_bank.count(letter):
                return True
            else: 
                return False
    

def check_letters_intersecting(word, letter_bank):
    word_set = set()
    if not word.upper(): 
        return False
    for letter in word.upper(): 
        word_set.add(letter)
    result = word_set & set(letter_bank)
    if len(result) == len(set(word)):
        return True
    else: 
        return False


# Wave 3

def score_word(word):
    score_chart = {
        1:["A","I","E","O","U","L","N","R","S","T"],
        2:["D","G"],
        3:["B","C","M","P"],
        4:["F","H","V","W","Y"],
        5:["K"],
        8:["J","X"],
        10:["Q","Z"]
    }
    extra_score_chart = [7, 8, 9, 10]
    total_score = 0
    letter_list = []

    if word == "":
        return total_score
    for letter in word.upper():
        letter_list.append(letter)
    for letter in letter_list:
        for point, letters in score_chart.items():
            if letter in letters:
                total_score += point
    if len(word) in extra_score_chart:
        total_score += 8
    return total_score 

# def get_highest_word_score(word_list):
#     word_scores = {}
#     highest_score_list = []

#     for word in word_list: 
#         word_scores[word] = score_word(word)
#     highest = max(word_scores.values())
#     for word, score in word_scores.items():
#         if score == highest:
#             highest_score_list.append(word)
#     if len(highest_score_list) == 1:
#         highest_score_list.append(score_word(highest_score_list[0]))
#         return tuple(highest_score_list)
#     elif len(highest_score_list) > 1:
#         shortest_word = min(highest_score_list, key=len)
#         longest_word = max(highest_score_list, key=len)
#         if len(longest_word) == 10:
#             return highest_score(longest_word) 
#         else:
#             for item in highest_score_list: 
#                 if len(item) == len(shortest_word):
#                         return highest_score(item)
#             return highest_score(item) 

def get_highest_word_score(word_list):
    word_scores = {}
    highest_score_list = {}

    for word in word_list: 
        word_scores[word] = score_word(word)
    highest = max(word_scores.values())
    for word, score in word_scores.items():
        if score == highest:
            highest_score_list[word] = score

    if len(highest_score_list) == 1:
        return highest_score(next(iter(highest_score_list)))
    elif len(highest_score_list) > 1:
        shortest_word = min(highest_score_list)
        # print(shortest_word)
        longest_word = max(highest_score_list)
        print(longest_word)

        if len(shortest_word) == 10:
            return highest_score(longest_word) 
        else:
            for item in highest_score_list: 
                if len(item) == len(longest_word):
                        return highest_score(item)
            return highest_score(item) 



def highest_score(word):
    winning_list=[]
    winning_list.append(word)
    winning_list.append(score_word(word))
    return tuple(winning_list)

