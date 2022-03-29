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

def draw_letters(LETTER_POOL):
    letter_list = []
    copy_dict = copy.copy(LETTER_POOL)

    for i in range(10):
        letter = random.choice(list(copy_dict))
        copy_dict[letter] -= 1
        letter_list.append(letter)
        if copy_dict[letter] < 1:
            copy_dict.pop(letter)

    return letter_list

def uses_available_letters(word, letter_bank):
    list_copy = letter_bank.copy()

    for character in word:
        character = character.capitalize()
        if character in list_copy:
            list_copy.remove(character)
        else:
            return False
    
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass