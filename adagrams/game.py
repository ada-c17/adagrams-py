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
    '''Function draw_letters returns 10 randomly drawn letters (aka letter_bank) based on the contraints laid out within the LETTER_POOL dictionary /
    (i.e. letters and quantity of letters available).

    No parameters passed

    Returns:
    letter_bank (list): a list of 10 strings characters representing 10 randomly drawn letters
    '''
    letters = list(LETTER_POOL.keys())
    
    letter_quantity = list(LETTER_POOL.values())

    pool_strings = []

    pool = []

    for i in range(len(letters)):
        pool_strings.append(letters[i] * letter_quantity[i])

    for string in pool_strings:    
        for letter in string:
            pool.append(letter)

    letter_bank = list(random.sample(pool, 10))
    return letter_bank
            

def uses_available_letters(word, letter_bank):
    '''Function uses_available_letters has two parameters (word and letter_bank) and returns either True or False.

    Parameters: 
    word (string): a word composed of letters within the letter_bank
    letter_bank (list): a list of 10 string characters representing 10 randomly drawn letters

    Returns:
    boolean: True if all letters in word are in the letter_bank, False if not
    '''

    if isinstance(word, str) and len(word) <= 10:
        word_up = word.upper()
        bank_dict = {}
        word_dict = {}

        for letter in letter_bank:
            if letter in bank_dict:
                bank_dict[letter] += 1
            else:
                bank_dict[letter] = 1

        for letter in word_up:
            if letter in word_dict:
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1  
        
        for letter in word_up:
            if word_dict[letter] <=  bank_dict[letter]:
                for letter in word_up:
                    if letter not in letter_bank:
                        return False
                return True
            return False
    return False


def score_word(word):
    '''Function score_word has one parameter (word) and returns the score of that word as defined by the Adagrams game (see below score chart).

    Parameters: 
    word (string): a word composed of letters within the letter_bank

    Returns:
    score (int): the cumulative point value of the word based on the score chart and word length, where applicable
    '''
    score = 0

    one_point = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    two_points = ["D", "G"]
    three_points = ["B", "C", "M", "P"]
    four_points = ["F", "H", "V", "W", "Y"]
    five_points = ["K"]
    eight_points = ["J", "X"]
    ten_points = ["Q", "Z"]
    long_word_bonus = [7, 8, 9, 10]

    word_up = word.upper()
    
    if len(word_up) in long_word_bonus:
        score += 8

    for letter in word_up:
        if letter in one_point:
            score += 1
        elif letter in two_points:
            score += 2
        elif letter in three_points:
            score += 3
        elif letter in four_points:
            score += 4
        elif letter in five_points:
            score += 5
        elif letter in eight_points:
            score += 8
        elif letter in ten_points:
            score += 10

    return score

def get_highest_word_score(word_list):
    '''Function get_highest_word_score has one parameter (word_list) and returns the highest scoring word. Furthermore, the function also dictates /
    what word would win in the case of a tie.

    Parameters:
    word_list (list): a list of strings representing all of the words that the user was able to create given each letter_bank drawn.

    Return:
    word, score (tuple): word, a string, represents the word that earned the most points and score, an integer, represents the cumulative /
    point value of the highest scoring word based on the score chart and word length, where applicable
    '''
    tie_score_check = 0
    score_per_word = {}

    for word in word_list:
        score = score_word(word)
        score_per_word[word] = score
    
    highest_scoring_word = max(score_per_word.values())
    shortest_length_if_tie = min(len(word) for word in score_per_word if score_per_word[word] == highest_scoring_word)

    for word, score in score_per_word.items():
        if score == highest_scoring_word:
            tie_score_check += 1
    
    for word, score in score_per_word.items():
        if tie_score_check > 1:
            if len(word) == 10 and score == highest_scoring_word:
                return word, score
        
    for word, score in score_per_word.items():
        if score == highest_scoring_word and tie_score_check == 1:
            return word, score
        elif score == highest_scoring_word and tie_score_check > 1:
            if len(word) == shortest_length_if_tie:
                return word, score
    

