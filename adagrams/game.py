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
    a_z_list = [key for key in LETTER_POOL]
    
    letter_frequency = copy.deepcopy(LETTER_POOL)

    letter_bank = []
    while len(letter_bank) < 10:
        letter = random.choice(a_z_list)
        if letter_frequency[letter] == 0: 
            continue 
        letter_frequency[letter] -= 1
        letter_bank.append(letter)

    return letter_bank


        
    #To get single letter, turn LETTER_POOL keys into list (a-z)
    #random.choice the list
    #make deep copy of LETTER_POOL
    #while loop
    #update talley of LETTER_POOL deepcopy
    #if statement for if value is zero, pick another letter
    

def uses_available_letters(word, letter_bank):
    #if statement for word less than len(letter_bank)
    #create letter bank dict w/ talley frequency
    #for loop through word 
    #if statement for letter in letter bank dict, subtract frequency
    #if scenario for value at letter bank dict == 0, return false 
    #return true at end if all works
    pass

def score_word(word):
    #dictioanry where point score are keys and letter in array as values
    #initialize variable to keep track of score
    #if word is greater than 7 in length, add 10 points 
    #for loop to loop through word - accesses single letter of user's input
    #for loop to loop through dicitonary 
    #the scores will be in str so need to convert to int
    #if statement for if letter in letter array - talley total points
    pass

def get_highest_word_score(word_list):
    #initialize max_score list - will tuple of word, score
    #####
    #variable for length of the word
    #variable for max score 
    ######
    #for word in word list
    #call score_word() function -- append word & score to max_score_list
    #for loop to loop through max_score_list to meet requirements

    pass

draw_letters()


