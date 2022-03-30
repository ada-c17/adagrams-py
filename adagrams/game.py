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

SCORE_CHART = {
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K", ): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10
}

def draw_letters():
    # Create a copy of LETTER_POOL so it won't change the original data
    letter_pool_copy = LETTER_POOL.copy()   
    drawn_letters = []                           
    
    for i in range(10):
        # Choose a random letter 10 times
        letter = random.choice(list(letter_pool_copy.keys()))

        # Check letter qty, updating the LETTER_POOL_copy to reflect the distribution 
        #   if qty == 1 remove it from the copy so it won't be chosen again
        #   if qty > 1, decrease the qty by 1
        if letter_pool_copy[letter] == 1:
            del letter_pool_copy[letter]       
        else:
            letter_pool_copy[letter] -= 1
        drawn_letters.append(letter)
    return drawn_letters

def uses_available_letters(word, letter_bank):
    # Create a copy of letter_bank so it won't change the original data
    letter_bank_copy = letter_bank.copy()  
    word = word.upper() 
    
    # Check if each single character exists in leeter_bank_copy:
    #   if not, return False. 
    #   if yes, remove it from letter_bank_copy
    # If all letters in the letter_bank_copy, return True
    for char in word:                               
        if char not in letter_bank_copy:        
            return False            
        letter_bank_copy.remove(char)               
    return True

def score_word(word):
    score = 0
    word = word.upper()
    
    # Check each character in the word to find it's score in SCORE_CHART:
        # sum the score of each chacracter
    for letter in word:                            
        for char, value in SCORE_CHART.items():    
            if letter in char:                     
                score += value

    # If the lenght of the word more than 6 characters, add 8 to the total score
    if len(word) > 6:
        score += 8

    return score


def get_highest_word_score(word_list):
    words_score = {}
    max_value = 0

    # Create a dictionary of word: score. Find the highest score between current and previous word.
    for word in word_list:  
        words_score[word] = score_word(word)
        max_value = max(max_value, words_score[word]) 

    # Create a list of all words that have the highest score.
    words_max_value = [word for word, score in words_score.items() if score == max_value]

    # Check if words_max_value list has more than 1 word:
        # sort the list of words based on it's length
        # if the lenght of the word 10 letters:
            # return the first word with the lenght 10 letters and it's score
        # in all other cases return the first word in the list words_max_value as it has the fewest letters.
    if len(words_max_value) > 1: 
        words_max_value = sorted(words_max_value, key=len)
        for word in words_max_value:
            if len(word) == 10:
                return word, max_value  
    return words_max_value[0], max_value