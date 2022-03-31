import random


LETTER_QUANTITY_DICT = {
    'A' : 9, 'N' : 6 ,
    'B' : 2, 'O' : 8, 
    'C' : 2, 'P' : 2, 
    'D' : 4, 'Q' : 1, 
    'E' : 12,'R' : 6,
    'F' : 2, 'S' : 4, 
    'G' : 3, 'T' : 6,
    'H' : 2, 'U' : 4,
    'I' : 9, 'V' : 2, 
    'J' : 1, 'W' : 2,
    'K' : 1, 'X' : 1, 
    'L' : 4, 'Y' : 2,
    'M' : 2, 'Z' : 1}

def draw_letters():
    letter_list = []

    # changes the dictionary into a list
    # the counter to ensure the distribution of letters
    for letter, quantity in LETTER_QUANTITY_DICT.items():
        counter = 0
        while counter < quantity:
            letter_list.append(letter)
            counter += 1
    
    # draws 10 letters from the letter_list
    letter_bank = random.sample(letter_list, 10)

    return letter_bank




def uses_available_letters(word, letter_bank):
#    return true or false if the word has the correct letter quantities in the word bank
#  Check if word is valid 
# Loop through word to append to list. List for element in the word
# - Helper function if letter is in list- 
# - Return False if not in list
# If letter.count in word <= letter count in list Return True,
#  If not correct quantity return False
    
    if not check_letters_intersecting(word,letter_bank):
        return False
    elif check_letters_intersecting(word,letter_bank):
        for letter in word.upper(): 
            if word.count(letter) <= letter_bank.count(letter):
                return True
            else: 
                return False
    

    # Function checks if all letters in word are in letter bank
def check_letters_intersecting(word, letter_bank):
    # makes word into a set for comparison
    word_set = set()
    # guard clause
    if not word.upper(): 
        return False
        # for each letter in word add to word set
    for letter in word.upper(): 
        word_set.add(letter)
        # compares set with intersection for overlapping letters
    result = word_set & set(letter_bank)
    # if all the same letters in both sets they will have equal lengths
    if len(result) == len(set(word)):
        return True
    else: 
        return False


# Wave 3

def score_word(word):
    score_chart = {
        1:["A","I","E","O","U","L","N","R","S","T"],
        2:["D","G"],
        3:["B","C","M","P"],
        4:["F","H","V","W","Y"],
        5:["K"],
        8:["J","X"],
        10:["Q","Z"]
    }
    extra_score_chart = [7, 8, 9, 10]
    total_score = 0
    letter_list = []

    # initalize check to see if the word is empty
    if word == "":
        return total_score

    # adds each letter in word to the letter_list
    for letter in word.upper():
        letter_list.append(letter)

    # loops through the letter_list
    # checks each letter against the score_chart dictionary
    for letter in letter_list:
        for point, letters in score_chart.items():
            if letter in letters:
                total_score += point

    # final check for extra points! 
    if len(word) in extra_score_chart:
        total_score += 8

    return total_score 



def get_highest_word_score(word_list):

    # Empty dictionary to store word and scores
    # get key(s) of dictionary with highest score
    # if length of highest score == 1 --> return 
    # If only
    # If word == 10 letters or min length ---> otherwise first one in length. 
    # returns tuple


    word_scores = {}
    highest_score_list = []
    # Goes thru each word and adds word as key and score as value to dictionary
    for word in word_list: 
        word_scores[word] = score_word(word)
# evaluates dictionary for highest score - record integer
    highest = max(word_scores.values())
    # goes through every every key, accesses value--> when value is the same as the high score, add to list 
    for word, score in word_scores.items():
        if score == highest:
            highest_score_list.append(word)
    # when the length of the list is 1, return the tuple of the word and score
    if len(highest_score_list) == 1:
        highest_score_list.append(score_word(highest_score_list[0]))
        return tuple(highest_score_list)
        # when the length of the list is greater than one, meaning ties
    elif len(highest_score_list) > 1:
        shortest = min(highest_score_list, key=len)
        longest_word = max(highest_score_list, key=len)
        if len(longest_word) == 10:
            return highest_score(longest_word) 
        else:
            for item in highest_score_list: 
                if len(item) == len(shortest):
                        return highest_score(item)
            return highest_score(item) 

            
def highest_score(word):
    winning_list=[]
    winning_list.append(word)
    winning_list.append(score_word(word))
    return tuple(winning_list)

