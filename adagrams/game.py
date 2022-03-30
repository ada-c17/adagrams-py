from random import randint
from copy import deepcopy

LETTER_POOL = [
                "A", "A", "A", "A", "A", "A", "A", "A", "A",
                "B", "B",
                "C", "C",
                "D", "D", "D", "D", 
                "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
                "F", "F",
                "G", "G", "G",
                "H", "H",
                "I", "I", "I", "I", "I", "I", "I", "I", "I", 
                "J",
                "K",
                "L", "L", "L", "L", 
                "M", "M",
                "N", "N", "N", "N", "N", "N", 
                "O", "O", "O", "O", "O", "O", "O", "O", 
                "P", "P",
                "Q",
                "R", "R", "R", "R", "R", "R", 
                "S", "S", "S", "S", 
                "T", "T", "T", "T", "T", "T", 
                "U", "U", "U", "U", 
                "V", "V",
                "W", "W",
                "X",
                "Y", "Y",
                "Z"
    ]


def draw_letters():
    letter_pool_copy = deepcopy(LETTER_POOL)
    drawn_letters = []
    while len(drawn_letters) < 10:
        rand_index = randint(0, len(letter_pool_copy)-1)
        drawn_letters.append(letter_pool_copy.pop(rand_index))
    return drawn_letters


def uses_available_letters(word, letter_bank):
    letter_bank_copy = deepcopy(letter_bank)
    word = word.upper()
    valid_word = True

    for letter in word:
        if letter not in letter_bank_copy:
            valid_word = False
        else:
            letter_bank_copy.remove(letter)
    
    return valid_word

def score_word(word):
    
    letter_dict = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 
    'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10,
}

    word_score = 0
    
    if word == None:
        return None
    else:
        word = word.upper()
        for letter in word:
            word_score += letter_dict[letter]
        if len(word) >= 7:
            word_score += 8
    return word_score

def get_highest_word_score(word_list):
   
    best_word = {
        "word" : "",
        "score" : 0
    }

    for word in word_list:
        score = score_word(word)
        if score > best_word["score"]:
            best_word["score"] = score
            best_word["word"] = word
        elif score == best_word["score"]:
            if len(word) == 10 and len(best_word["word"]) != 10:
                best_word["score"] = score
                best_word["word"] = word
            elif len(word) < len(best_word["word"]) and len(best_word["word"]) != 10:
                best_word["score"] = score
                best_word["word"] = word

    return (best_word["word"], best_word["score"])