import random 
import copy 
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
    #PSEUDOCODE 
    #To get single letter, turn LETTER_POOL keys into list (a-z)
    #random.choice the list
    #make deep copy of LETTER_POOL
    #while loop
    #update talley of LETTER_POOL deepcopy
    #if statement for if value is zero, pick another letter

    #creating alphabet list from LETTER_POOL keys
    a_z_list = [key for key in LETTER_POOL]
    
    #making copy of available letters w/ distribution of letters
    letter_frequency = copy.deepcopy(LETTER_POOL)
    
    #initializing letter bank list
    letter_bank = []

    #while loop to create letter bank with 10 letters
    while len(letter_bank) < 10:
        #randomly choosing letter from available alphabet list
        letter = random.choice(a_z_list)
        #catching scenario if current letter distrubution is zero
        if letter_frequency[letter] == 0: 
            continue 
        #else if letter is available, subtract from available distrubution
        letter_frequency[letter] -= 1
        letter_bank.append(letter)
    return letter_bank



def uses_available_letters(word, letter_bank):
    #PSEUDO CODE
    #if statement for word less than len(letter_bank)
    #create letter bank dict w/ talley frequency
    #for loop through word 
    #if statement for letter in letter bank dict, subtract frequency
    #if scenario for value at letter bank dict == 0, return false 
    #return true at end if all works

    #catching scenario where user enters lowercased letters
    word = word.upper()

    #catching scenario where user enters word longer than 10 letters
    if len(word) > len(letter_bank):
        return False

    #initalizing letter frequency dictionary for talley
    letter_frequency = {}

    #for looping through our letter bank input to create letter freq dictionary
    for letter in letter_bank:
        #if statement for if the letter in the letter bank is in our letter freq dict
        #then talley one, else create new key-value pair
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
    
    #for looping through user's word to check if letter is available in letter freq dict
    for letter in word:
        #if statement for if letter is available in letter freq dict and freq is not zero
        if letter in letter_frequency and letter_frequency[letter] != 0:
            letter_frequency[letter] -= 1
        else:
            return False
    return True



def score_word(word):
    #PSEUDO CODE
    #dictioanry where point score are keys and letter in array as values
    #initialize variable to keep track of score
    #if word is greater than 7 in length, add 10 points 
    #for loop to loop through word - accesses single letter of user's input
    #for loop to loop through dicitonary 
    #the scores will be in str so need to convert to int
    #if statement for if letter in letter array - talley total points

    #catching scenario where user enters lowercased letters   
    word = word.upper()
    
    #score chart from project instruction
    SCORE_CHART = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]		
    }

    #initalize score variable to track current score
    score = 0

    #catching scenario if word is greater than or equal to 7, automatically add 8 points
    if len(word) >= 7:
        score += 8
    
    #for looping through user's word input to calc score
    for letter in word:
        for key, value in SCORE_CHART.items():
            #looping through letter array to determine score of current letter
            for available_letter in value:
                if letter == available_letter:
                    score += key 
    
    return score 


def get_highest_word_score(word_list):
    #PSEUDO CODE
    #initialize max_score list - will tuple of word, score
    #####
    #variable for length of the word
    #variable for max score 
    ######
    #for word in word list
    #call score_word() function -- append word & score to max_score_list
    #for loop to loop through max_score_list to meet requirements
    #for tie breaker:
    #if statement current score is equal to max store 

    
    #initalize max score list which is list of tuples
    max_score_list = []

    #for looping through input to determine score for each word
    #and append to max score list
    for word in word_list:
        word_score = score_word(word)
        max_score_list.append((word, word_score))
    # print(max_score_list)

    #initialize variable to track max score/current word
    max_score = 0
    min_length = 0
    max_pair = None
    
    #looping through available words/scores
    for pair in max_score_list:
        #scenario for if current score is greater than current max score, 
        #reassign all variables to the current word/score
        if pair[1] > max_score:
            max_score = pair[1]
            min_length = len(pair[0])
            max_pair = pair
        #scenario for tie breaker 
        elif pair[1] == max_score:
            #tie breaker bullet point 1 or bullet point 2
            if (len(pair[0]) < min_length and min_length != 10) or \
                (len(pair[0]) == 10 and len(max_pair[0]) != 10):
                max_pair = pair
                min_length = len(pair[0])
            #tie breaker bullet point 3 met when none of the conditions above are true
    return max_pair


    




