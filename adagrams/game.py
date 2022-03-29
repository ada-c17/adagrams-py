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
    #letter_bank_copy = copy.copy(letter_bank)
    #letter_bank_copy = letter_bank.copy()
    # no need to create a copy as we are not modifying the letter bank
    # we ARE touching it, but that's okay!! We're not adding or removing
    # anything to the list. 
    # I was getting a weird KeyError sometimes if I tried to break it in the 
    # playtester (like if I was inputting "HOG" instead of "DOG" if the 
    # letters for "DOG" where only available) after I got all the tests to run 
    # so I put in a try/except to catch it but there is probably a much more
    # elegant solution
    try:
    #converts the input to uppercase
        word = word.upper()
    
    #splits word into a list
        guessed_letters = list(word)

    #so this is for the third test mostly
    #counts the amount of times that each letter appears in each list,
    #and if it's greater than the count of the letters in the letter bank, return False
        letter_count_guessed_letters = {}
        letter_count_letter_bank = {}
    
        count = 0
        for letter in guessed_letters:
            count += 1
            letter_count_guessed_letters[letter] = count

    #reinit count just in case of anything crazy.....
        count = 0
        for letter in letter_bank:
            count += 1
            letter_count_letter_bank[letter] = count
    
    #does the comparison stuff
        for letter, count in letter_count_guessed_letters.items():
            if count > letter_count_letter_bank[letter]:
                return False
            else:
        #all() returns True if all guessed letters are in the letter bank, False if not
        #basically it's saying, hey here's this loop, are we getting True every time
        #if not, we're doing to return False
        #I also had to use a list comprehension, which is t r i c k y
        #I tried to escape using one as they are awful to explain or understand
        #I could not. T_T
        
                uses_letters = all(letter in letter_bank for letter in guessed_letters)
                return uses_letters
    
    except KeyError:
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