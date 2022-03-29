import random

# Return list of ten strings
# Each string is one letter
# Import random

# Create dictionary 
# Create list
# Iterate 10 times
# If the number in the list equal to number in dict, continue without adding
### If not, append to list


def draw_letters():
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
    letters = []
   
    while len(letters) < 10:
        letter = random.choice(list(LETTER_POOL))
        if LETTER_POOL[letter] == 0:
            continue
        else:
            letters.append(letter)
            LETTER_POOL[letter] -= 1
   
    return letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
