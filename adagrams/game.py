from random import randint

def draw_letters():
    #define list of available letters
    #take 10 random rolls each with one less number
    #pop each out between rolls and store in list
    #return list of rolled letters
    letter_bank = ['A','A','A','A','A','A','A','A','A','B','B','C','C','D','D','D','D','E','E','E','E','E','E','E','E','E','E','E','E','F','F','G','G','G','H','H','I','I','I','I','I','I','I','I','I','J','K','L','L','L','L','M','M','N','N','N','N','N','N','O','O','O','O','O','O','O','O','P','P','Q','R','R','R','R','R','R','S','S','S','S','T','T','T','T','T','T','U','U','U','U','V','V','W','W','X','Y','Y','Z']

    letter_list = []

    for roll in range(0,10):
        remove_letter = randint(0, len(letter_bank)-1)
        letter = letter_bank.pop(remove_letter)
        letter_list.append(letter)
    return letter_list


def uses_available_letters(word, letter_bank):
    #make input uppercase
    #make copy of list of letters
    #loop through the word index string
    #loop through letter list and pop found letter
    #if letter not found return false
    #return true
    word = word.upper()
    letter_bank_copy = letter_bank.copy()

    for letter in word:
        if letter not in letter_bank_copy:
            return False
        for i in range(len(letter_bank_copy) - 1):
            if letter == letter_bank_copy[i]:
                letter_bank_copy.pop(i)
                continue

    return True


def score_word(word):
    #test for zero length
    #define list of dictionaries for points
    #upper() the word
    #len()>6 for 8 additional points
    #loop through word
    #  lookup point value in dictionary
    #  add to sum
    #return sum
    
    score_dict = {  'A' : 1, 'E' : 1, 'I' : 1, 'O' : 1, 'U' : 1, 
                    'L' : 1, 'N' : 1, 'R' : 1, 'S' : 1, 'T' : 1,
                    'D' : 2, 'G' : 2,
                    'B' : 3, 'C' : 3, 'M' : 3, 'P' : 3,
                    'F' : 4, 'H' : 4, 'V' : 4, 'W' : 4, 'Y' : 4,
                    'K' : 5,
                    'J' : 8, 'X' : 8,
                    'Q' : 10, 'Z' : 10}

    word = word.upper()
    score = 0

    if len(word) > 6:
        score += 8
    for letter in word:
        score += score_dict[letter]
    return score
    

def get_highest_word_score(word_list):
    #define word,score tuple
    #loop through passed list
    #  use wave 3 to calculate score
    #  compare score
    #  compare length is same
    #    replace tuple with index word and score
    #return tuple
    highest_score = ("",0)
    score = 0

    for word in word_list:
        score = score_word(word)
        if score > highest_score[1]:
            highest_score = word, score
        elif score == highest_score[1]:
            if len(highest_score[0]) == 10:
                continue
            elif len(word) == 10: 
                highest_score = word, score
            elif len(highest_score[0]) > len(word):
                highest_score = word, score

    return highest_score

