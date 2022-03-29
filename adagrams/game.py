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
    word = word.upper()
    if len(word) > len(letter_bank):
        return False
    letter_frequency = {}
    for letter in letter_bank:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
    
    for letter in word:
        if letter in letter_frequency and letter_frequency[letter] != 0:
            letter_frequency[letter] -= 1
        else:
            return False

    return True

    #if statement for word less than len(letter_bank)
    #create letter bank dict w/ talley frequency
    #for loop through word 
    #if statement for letter in letter bank dict, subtract frequency
    #if scenario for value at letter bank dict == 0, return false 
    #return true at end if all works

# print(uses_available_letters("bac", ["a", "b", "c", "d", "e", "o", "g", "a", "f", "m"]))


def score_word(word):
    word = word.upper()
    score_chart = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]		
    }
    score = 0

    if len(word) >= 7:
        score += 8
    
    for letter in word:
        for key, value in score_chart.items():
            for available_letter in value:
                if letter == available_letter:
                    score += key 
    
    return score 


    #dictioanry where point score are keys and letter in array as values
    #initialize variable to keep track of score
    #if word is greater than 7 in length, add 10 points 
    #for loop to loop through word - accesses single letter of user's input
    #for loop to loop through dicitonary 
    #the scores will be in str so need to convert to int
    #if statement for if letter in letter array - talley total points

def get_highest_word_score(word_list):
    max_score_list = []

    for word in word_list:
        word_score = score_word(word)
        max_score_list.append((word, word_score))
    # print(max_score_list)

    max_score = 0
    min_length = 0
    max_pair = None
    for pair in max_score_list:
        print(pair)
        print(max_score)
        print(min_length)
        print("")
        if pair[1] > max_score:
            max_score = pair[1]
            min_length = len(pair[0])
            max_pair = pair
        elif pair[1] == max_score:
            if len(pair[0]) == min_length:
                print("made in first if statement")
            elif len(pair[0]) == 10 and len(max_pair[0]) != min_length:
                print("made it in first elif statemnet")
                max_pair = pair
            elif len(pair[0]) < min_length and min_length != 10:
                print("made it in last elif statement")
                max_pair = pair
        print("")
        print(max_score)
        print(min_length)
        print(max_pair)
        print("")
    return max_pair
    


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
        #

    
print(get_highest_word_score(["AAAAAAAAAA", "BBBBBB"]))


# print(score_word("dog"))
# print(score_word("XXXXXXX"))