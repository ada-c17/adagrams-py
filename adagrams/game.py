import random
import string
DRAWN_LETTERS_TOTAL = 10

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

SCORE_CHART = {
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
    # randomly draw 10 letters, should match the letter pool rules
    # create a dictionary to keep track of our {current drawn letter : count}
    # update letter count in the dict
    # check if letter count is over LETTER_POOL[letter]
    # if yes, remove the letter
    # if no, do nothing
    # keep drawing until have 10 letters
    # returns an array of 10 letters
    result = []
    letter = ''
    drawn_letters = {}
    
    while len(result) < DRAWN_LETTERS_TOTAL:
        letter = random.choice(string.ascii_uppercase)
        result.append(letter)   
        if letter not in drawn_letters:
            drawn_letters[letter] = 1
        else: 
            drawn_letters[letter] += 1
        
        if drawn_letters[letter] > LETTER_POOL[letter]:
            result.remove(letter)        
    return result

def uses_available_letters(word, letter_bank):
    word = word.upper()
    
    letter_bank_dict = {}
    word_dict = {}
    # Dictionary of letters in user's hand
    for letter in letter_bank:
        if letter not in letter_bank_dict:
            letter_bank_dict[letter] = 1
        else:
            letter_bank_dict[letter] +=1
    
    for letter in word:
        if letter not in letter_bank_dict:
            return False
        if letter not in word_dict:
            word_dict[letter] = 1
        else:
            word_dict[letter] += 1
        if word_dict[letter] > letter_bank_dict[letter]:
            return False
    return True


def score_word(word):
    word = word.upper()
    points = 0
    for letter in word:
        points += SCORE_CHART[letter]

    if len(word) >= 7:
        points += 8

    return points

def get_highest_word_score(word_list):
    hightest_score = 0
    hightest_word = ""

    for word in word_list:
        score = score_word(word)
        if score > hightest_score:
            hightest_score = score
            hightest_word = word
    return (hightest_word,hightest_score)
