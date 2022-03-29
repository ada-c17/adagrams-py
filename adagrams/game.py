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
    '''This function returns 10 random letter tiles. Frequency of letters determined by LETTER_POOL'''
    # letter_freq = {}
    letters = []
    letter_pool_copy = LETTER_POOL.deepcopy()
    while len(letters) < 10:
        for letter in letter_pool_copy:
            if letter_pool_copy[letter] == 0:
                letter_pool_copy.remove(letter)
            else:
                random_letter = random.choice(letter_pool_copy)
                letters.append(random.choice(random_letter))
                letter_pool_copy[random_letter] = letter_pool_copy[random_letter]-1
    return letters


    '''PSUEDOCODE:
    1) Make deep copy of LETTER_POOL
    2) if LETTER_POOL.deepcopy value = 0; remove
        3) Generate random letter from current LETTER_POOL.deepcopy- 
        4) Find letter in LETTER_POOL.deepcopy 
        5) -1 from value
        6) append letter to letters[]
    7) Return letters[]'''


    # # Generate 10 random letters
    # for letter in LETTER_POOL:
    #     letter_pool_keys.append(letter)
    # for i in range(10):
    #     letters.append(random.choice(letter_pool_keys))
    # print(f"Debug: letters = {letters}")
    
    # # Create frequency map of letters
    # for letter in letters:
    #     if letter in letter_freq:
    #         letter_freq[letter] += 1
    #     else:
    #         letter_freq[letter] = 1
    # print(f"Debug: letter_freq = {letter_freq}")
    
    # # Check letter_freq against LETTER_POOL freq & replace as necessary
    # for letter in letters:        
    #     if letter_freq[letter] > LETTER_POOL[letter]: # <-- CHECK THIS LINE
    #         print(letter_freq[letter])
    #         print(LETTER_POOL[letter])
    #         letters.remove(letter)
    # print(f"Debug: letters = {letters}")
    # while len(letters) != 10:    
    #     letters.append(random.choice(letter_pool_keys))
            
    # print(f"DEBUG: letters = {letters}")
    # return letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

print(draw_letters())