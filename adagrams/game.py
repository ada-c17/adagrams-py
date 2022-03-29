import copy 
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

def draw_letters():
    ten_letters = []
    no_change_letters = LETTER_POOL.copy()
    for i in range(10):
        random_letter = random.choice(list(LETTER_POOL))
        if no_change_letters[random_letter] > 0:
            ten_letters.append(random_letter)
            no_change_letters[random_letter] -= 1
    return ten_letters

def uses_available_letters(word, letter_bank):
    letter_count = 0
    letter_copy = letter_bank[:]
    for letter in word:
        if letter.upper() in letter_copy:
            letter_copy.remove(letter.upper())
            letter_count += 1
    return letter_count == len(word)
            
 

def score_word(word):
    sum = 0
    for char in word:
        if len(char) >= 7 and len(char) <= 10:
            sum += 8
    return sum
          
          
          
          
            # if "A" or "E" or "I" or "O" or "U" or "L" or "N" or "R" or "S" or "T" == char:
            #     sum += 1
            # elif "D" or "G" == char:
            #     sum += 2
            # elif "B" or "C" or "M" or "P" == char:
            #     sum += 3
            # elif "F" or "H" or "V" or "W" or "Y" == char:
            #     sum += 4
            # elif "K" == char:
            #     sum += 5
            # elif "J" or "X" == char:
            #     sum += 8
            # else:
            #     sum += 10




def get_highest_word_score(word_list):
    pass

