
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


def get_highest_word_score(word_list):
    word_scores = {}

    for word in word_list: 
        word_scores[word] = score_word(word)
    
    highest_score_dict = {word:score for word, score in word_scores.items() if score == max(word_scores.values())}

    if len(highest_score_dict) == 1:
        return convert_dict_to_tuple(highest_score_dict)
    else:
        for word, score in sorted(highest_score_dict.items()):
            winning_word = {}
            shortest_word = min(len(x) for x in highest_score_dict.keys())
            if len(word) == 10:
                winning_word[word] = score
                return convert_dict_to_tuple(winning_word)
            elif len(word) == shortest_word:
                winning_word[word] = score
                return convert_dict_to_tuple(winning_word)

def convert_dict_to_tuple(highest_score_dict):
    highest_score_list = []
    for word, score in highest_score_dict.items():
        highest_score_list.append(word)
        highest_score_list.append(score)
    return tuple(highest_score_list)

