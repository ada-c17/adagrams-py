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

SCORE_DICTIONARY = {
        "A": 1,
        "E": 1,
        "I": 1,
        "O": 1,
        "U": 1,
        "L": 1, 
        "N": 1,
        "R": 1,
        "S": 1,
        "T": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4, 
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10,
    }

def draw_letters():

    letter_pool_copy = copy.deepcopy(LETTER_POOL)
    player_hand = []
    letter_weights = list(LETTER_POOL.values())
    letter_pool_list = list(LETTER_POOL.keys())

    while len(player_hand) < 10:
        letter = (random.choices(letter_pool_list, weights= (letter_weights)))

        if letter_pool_copy[letter[0]] == 0:
            continue
        else:
            letter_pool_copy[letter[0]] -= 1

        player_hand.append(letter[0])

    return player_hand


def uses_available_letters(word, letter_bank):
    letter_bank_dict = {}
    word = word.upper()

    for letter in letter_bank:
        if letter in letter_bank_dict:
            letter_bank_dict[letter] += 1
        else:
            letter_bank_dict[letter] = 1

    for character in word:
        if character in letter_bank_dict and letter_bank_dict[character] > 0:
            letter_bank_dict[character] -= 1
        else:
            return False
    
    return True
    
def score_word(word):
    
    word_score = 0
    converted_string = word.upper()
    for letter in converted_string:
        if letter in SCORE_DICTIONARY:
            word_score += SCORE_DICTIONARY[letter]
    if len(word) >= 7:
        word_score += 8  
        
    return word_score
    
def get_highest_word_score(word_list):

    best_word = [word_list[0], score_word(word_list[0])]

    for word in word_list:
        if score_word(word) > best_word[1]:
            best_word[0] = word
            best_word[1] = score_word(word)
        elif score_word(word) == best_word[1]:
            if len(best_word[0]) == 10:
                continue
            elif len(word) == 10:
                best_word[0] = word
            elif len(word) < len(best_word[0]):
                best_word[0] = word
    
    return tuple(best_word)

