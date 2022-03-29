from random import randint

def draw_letters():
    #define list of available letters
    letter_bank = ['A','A','A','A','A','A','A','A','A','B','B','C','C','D','D','D','D','E','E','E','E','E','E','E','E','E','E','E','E','F','F','G','G','G','H','H','I','I','I','I','I','I','I','I','I','J','K','L','L','L','L','M','M','N','N','N','N','N','N','O','O','O','O','O','O','O','O','P','P','Q','R','R','R','R','R','R','S','S','S','S','T','T','T','T','T','T','U','U','U','U','V','V','W','W','X','Y','Y','Z']
    letter_list = []
    for roll in range(0,10):
        #take 10 random rolls each with one less number
        
        remove_letter = randint(0, len(letter_bank)-1)
        
        #pop each out between rolls and store in list
        letter = letter_bank.pop(remove_letter)
        letter_list.append(letter)
    #return list of rolled letters
    return letter_list

def uses_available_letters(word, letter_bank):
    #make input uppercase
    #make copy of list of letters
    #loop through the word index string
    #loop through letter list and pop found letter
    #if letter not found return false
    #return true
    pass


def score_word(word):
    #test for zero length
    #define list of dictionaries for points
    #upper() the word
    #len()>6 for 8 additional points
    #loop through word
    #  lookup point value in dictionary
    #  add to sum
    #return sum
    pass

def get_highest_word_score(word_list):
    #test for zero length
    #define word,score tuple
    #loop through passed list
    #  use wave 3 to calculate score
    #  compare score
    #  compare length is same
    #    replace tuple with index word and score
    #return tuple
    pass