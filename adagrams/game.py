import random
import string
import copy
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
            # decrement counter
        if value == 0:
            continue
        letter_quantity[letter] -=1
        letter_bank.append(letter)
        counter -= 1
        
    # return a list of 10 letters   
    return letter_bank
    

def uses_available_letters(word, letter_bank):
    list_letters =  copy.deepcopy(letter_bank)   #set(letter_bank[:])
    for letter in word:
        if letter.upper() in list_letters:
            list_letters.remove(letter.upper())
        else:
            return False
        
    return True


def score_word(word):
    #create a dictionary of letters with corresponding points
    letter_points = {"A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2, "H":4, "I":1, "J":8, "K":5, "L":1,
                     "M":3, "N":1, "O":1, "P":3, "Q":10, "R":1, "S":1, "T":1, "U":1, "V":4, "W":4, "X":8,
                     "Y":4, "Z":10
                    }
    total_points = 0
    for letter in word:
        if letter.upper() in letter_points.keys():
            total_points += letter_points[letter.upper()]
    
    if len(word) >= 7 and len(word) <= 10:
            total_points += 8
            
    return total_points
    
    #total_score = sum(value[letter] for letter in letter_points.keys())
                      
def get_highest_word_score(word_list):
    # find word or words with max score
    score_dict = {}
    
    for word in word_list:
        score_dict[word] = score_word(word)
        
    max_score_words = []   
    max_score = max(score_dict.values())
    for word in word_list:
        if score_dict[word] == max_score:
            max_score_words.append(word)
    # apply tiebreaking logic to determine winning word
    # rule_01 prefer the word with the fewest letters
    # rule_02 if a word is ten letters long, it wins
    # rule_03 if multiple words with same score and same length, pick first in word_list
    winning_word = []
    if len(max_score_words) == 1:
        #winning_word.append(max_score)
        winning_word = [max_score_words[0], max_score]
        
    elif any(len(word) == 10 for word in max_score_words):
        for word in max_score_words:
            if len(word) == 10:
                winning_word = [word, max_score]
                break
    else:
        mini = min(max_score_words, key=len)
        for word in max_score_words:
            if word == mini:
                winning_word = [word, max_score]
                break
                

    #return a tuple with winning word and its score
    return tuple(winning_word)