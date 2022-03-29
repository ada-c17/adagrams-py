import random
import copy

def draw_letters():
    # Draws 10 random letters from the letter pool list
    letters = random.sample(create_letter_pool_list(), 10)
    return letters

def create_letter_pool_list():
    '''
    Adds all letters in the pool to a list based on their frequency
    and returns the list of letters.
    '''
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
    letter_pool_list = []
    for letter in LETTER_POOL.keys():
        for frequency in range(LETTER_POOL[letter]):
            letter_pool_list.append(letter)
    return letter_pool_list

def uses_available_letters(word, letter_bank):
    word = word.upper()

    # Creates a copy of letter bank so it can be mutated
    # without changing the original letter bank
    letter_bank_copy = copy.copy(letter_bank)
    
    # Checks if letter is in letter bank copy
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    letter_point_table = {
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
    points = 0
    word = word.upper()

    # Adds points for each letter based on point table
    for letter in word:
        points += letter_point_table[letter]
    
    # Adds extra points for length of word that is 7, 8, 9, or 10
    if 7 <= len(word) <= 10:
        points += 8
    
    return points

def get_highest_word_score(word_list):
    word_dict = {}
    max_score = 0
    winning_word = ""

    # Compare scores of each word and store the winning word and its score
    for word in word_list:
        score = score_word(word)
        word_dict[word] = score

        # If score for current iteration is greater than the max score,
        # store new winning word and its score
        if score > max_score:
            max_score = score
            winning_word = word
        elif score == max_score:
            # If score is tied and the length of the winning word is 10, 
            # the first word is the winning word
            if len(winning_word) == 10:
                continue
            # If score is tied and the length of the current word is 10,
            # but the previous winning word is not 10, 
            # then the current word is the new winning word
            elif len(word) == 10:
                winning_word = word
            # If score is tied and the length of the current word is less than
            # the winning word (but neither length is 10),
            # the current word is the new winning word
            elif len(word) < len(winning_word):
                winning_word = word
    
    # Return winning word and its score
    winning_word = tuple((winning_word, word_dict[winning_word]))
    return winning_word