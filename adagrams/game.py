import random
import copy

LETTER_POOL = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, 
    "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 8,
    "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1,
    "Y": 2, "Z": 1}
LETTERS = ["A","B","C","D","E","F","G","H","I","J","K","L", "M", "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def draw_letters():
    letters = copy.copy(LETTERS)
    # letters = LETTERS.copy()
    letter_pool = copy.copy(LETTER_POOL)
    # letter_pool = LETTER_POOL.copy()
    hand = []
    while len(hand) < 10:
        letter = random.choice(letters)
        for key, value in letter_pool.items():
            if letter == key and value > 0:
                letter_pool[key] -= 1
                hand.append(letter)
    return hand


def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.copy(letter_bank)
    # letter_bank_copy = letter_bank.copy()
    for letter in word:
        if letter not in letter_bank_copy:
            return False

# Has two parameters:
# word, the first parameter, describes some input word, and is a string
# letter_bank, the second parameter, describes an array of drawn 
# letters in a hand. You can expect this to be an array of ten strings, 
# with each string representing a letter
# Returns either True or False
# Returns True if every letter in the input word is available 
# (in the right quantities) in the letter_bank
# Returns False if not; if there is a letter in input that 
# is not present in the letter_bank or has too much of compared 
# to the letter_bank

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass