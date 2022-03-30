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

LETTER_SCORES = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def draw_letters():
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
    total = 0
    word = word.upper()
    
    if len(word) >= 7:
        total += 8
    for letter in word:
        total += LETTER_SCORES[letter]
    return total

def get_highest_word_score(word_list):
    highest_scoring_word = ""
    highest_score = 0    
    
    for word in word_list:
        word_score = score_word(word)
        if word_score > highest_score:
            highest_score = word_score
            highest_scoring_word = word
        elif word_score == highest_score:
            if len(highest_scoring_word) == 10:
                continue
            elif len(word) == 10:
                highest_scoring_word = word
            elif len(word) < len(highest_scoring_word):
                highest_scoring_word = word
                print(highest_scoring_word)
            
    return highest_scoring_word , highest_score
