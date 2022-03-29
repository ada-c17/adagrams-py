import random
def draw_letters():

    letters = ['A','A','A','A','A','A','A','A','A','B','B','C','C','D','D','D','D','E','E','E','E','E','E','E','E','E','E','E','E','F','F','G','G','G','H','H','I','I','I','I','I','I','I','I','I','J','K','L','L','L','L','M','M','N','N','N','N','N','N','O','O','O','O','O','O','O','O','P','P','Q','R','R','R','R','R','R','S','S','S','S','T','T','T','T','T','T','U','U','U','U','V','V','W','W','X','Y','Y','Z']
    
    return random.sample(letters, 10)


def uses_available_letters(word, letter_bank):
    letter_copy = letter_bank[:]
    for i in range(len(word)):
        letter = word[i]
        if letter.islower():
            letter = letter.upper()
        if letter in letter_copy:
            letter_copy.remove(letter)
        else:
            return False
    return True


def score_word(word):
    score_dictionary = {
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
        "Z": 10
    }
    score = 0
    for i in range(len(word)):
        char = word[i]
        if char.islower():
            char = char.upper()
        if char in score_dictionary:
            score += score_dictionary[char]
    if len(word) >6:
        score += 8
    return score

def get_highest_word_score(word_list):
    '''takes in a list of words, word_list, and returns the highest scoring word and its score as a tuple'''
    best_word = ("", 0)
    highest_score = 0
    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            best_word = (word, score)
        elif score == highest_score:
            if len(best_word[0]) == 10:
                continue
            elif len(word) == 10:
                best_word = (word, score)
            elif len(word) < len(best_word[0]):
                best_word = (word, score)
    return best_word
