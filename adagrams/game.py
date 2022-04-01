import random
from typing import Counter

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

    letter_list = []
    
    for key in LETTER_POOL:
        letter_list += key * LETTER_POOL[key]

    random.shuffle(letter_list) 

    output = letter_list[:10]

    return output


def uses_available_letters(word, letter_bank):

    for letter in word.upper():
        if word.upper().count(letter) > letter_bank.count(letter):
            return False
    return True

def score_word(word):


    score_chart = {"A" : 1 ,"E" : 1, "I" : 1, "O" : 1, "U": 1, "L" : 1 ,"N" : 1, "R" : 1,"S" : 1, "T": 1,"D" : 2,"G" :2 , "B" : 3,"C" :3,"M" :3,"P" :3,
                    "F" : 4,"H" : 4, "V" : 4, "W": 4, "Y": 4, "K":5 ,"J":8 ,"X": 8,"Q":10,"Z":10}
    score = 0 
    for elem in word:
        if elem.upper() in score_chart:
            score = score + score_chart[elem.upper()]

    if 7 <= len(word) <= 10:
        score = score + 8
    return score 
  

def get_highest_word_score(word_list):

    # Initialize max_score and max_word variables to store the output 
    max_score = 0
    max_word = ""
    
    for word in word_list:
        # Call helper function "score_word" to calculate the score of each word
        score = score_word(word)
        # If the score is greater than current max_score, update max_score and max_word
        if score > max_score:
            max_score = score
            max_word = word
        # In case of tie in score, we will check the length of current word and current max_word
        elif score == max_score:
            # The current max_word value will be updated if the len(word) and  len(max_word) != 10 & len(word) is less than len(max_word)
            if len(word) != 10 and len(max_word) != 10 and len(word) < len(max_word):
                max_word = word
            # The current max_word value will be updated if the len(word) == 10 and len(max_word) != 10  && len(word) is greater than len(max_word)
            elif len(word) == 10 and len(max_word) != 10 and len(word) > len(max_word):
                max_word = word
    return max_word,max_score



