import random
import string
def draw_letters():
    #create a list with the pool of letters
    letter_quantity = {"A":9, "B":2, "C":2, "D":4, "E":12 , "F":2, "G":3, "H":2, "I":9, "J":1,
                        "K":1, "L":4, "M":2, "N":6, "O":8, "P":2, "Q":1, "R":6, "S":4, "T":6, "U":4,
                       "V":2, "W":2, "X":1, "Y":2, "Z":1
                        }
    
    letter_bank = []
    #choose 10 random letters
    counter = 10
    while counter > 0: # Use a while loop
        # Get random number with randrange
        rand_i = random.randrange(ord("A"), ord("Z"))
        # Get the letter associated with that random number A-Z
        letter = chr(rand_i)
        # Get letter from dict
        value = letter_quantity[letter]
        # if the value is > 0
            # decrement the quantity
            # add to list of randomly chosen letters
            # decrement your counter
        if value <= 0:
            continue
        letter_quantity[letter] -=1
        letter_bank.append(letter)
        counter -= 1
        
    # return a list of 10 letters   
    return letter_bank
    

def uses_available_letters(word, letter_bank):
    list_letters = set(letter_bank[:])
    for letter in word:
        if letter.upper() in list_letters:
            list_letters.remove(letter.upper())
        else:
            return False
        
    return True


def score_word(word):
    #create a dictionary of letters with corresponding points
    #letter_points = {"A":1, "B":3, "C":3, "D": , "E":, "F":, "G":, }
    pass

def get_highest_word_score(word_list):
    pass