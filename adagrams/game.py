def draw_letters():
    #create a list with the pool of letters
    letter_quantity = {"A":9, "B":2, "C":2, "D":4, "E":12 , "F":2, "G":3, "H":2, "I":9, "J":1,
                        "K":1, "L":4, "M":2, "N":6, "O":8, "P":2, "Q":1, "R":6, "S":4, "T":6, "U":4,
                       "V":2, "W":2, "X":1, "Y":2, "Z":1
                        }
    
    letter_bank = []
    #choose 10 random letters
    while i in range(10): # Use a while loop
        # Get random number with randrange (hint ord())
        i = random.randrange(1,13)
        # Get the letter associated with that random number A-Z (hint ascii)
        if i != 0 and i in letter_quantity.values():
            list_of_letters.append(letter_quality[i])
        # Get letter from dict
        # if the value is > 0
            # decrement the quantity
            # add to list of randomly chosen letters
            # decrement your counter
        # else
            # We haven't found a letter available
    
    # return a list of 10 letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    #create a dictionary of letters with corresponding points
    letter_points = {"A":1, "B":3, "C":3, "D": , "E":, "F":, "G":, }

def get_highest_word_score(word_list):
    pass