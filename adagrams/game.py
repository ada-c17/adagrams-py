import copy
"""Explain why later"""
import random
"""Explain why later"""
import string 
"""Explain why later"""
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
    # Wave_01 starts on 203
    # import rand / random.choice(d.)
    # import copy / deepcopy
    #create while loop for if player_hand_list is less than 10
    # grab letters with rand
    #loop through letter pool to check if letter value is greater than 0
    #-> if yes, append letter into player_hand_list
    #-> if no, continue
    #-> subtract 1 from the letter's value in letter_pool
    #->
    # if enough quantity
    # subtract quantity for each letter
        # check to make sure it's > 0
    # COPY_LETTER_POOL = copy.deepcopy(LETTER_POOL)
    # random_letter = random.choice(list(COPY_LETTER_POOL))
    # print("***PRINT TEST***")
    # print(random_letter)
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
    player_hand = []
    random_letter = ""

    letter_count = len(player_hand)
    print(letter_count)
    while letter_count < 10:
        string.ascii_letters
        random_letter = random.choice(string.ascii_uppercase)
        
        if LETTER_POOL[random_letter] == 0:
            continue
        else:
            player_hand.append(random_letter)
            LETTER_POOL[random_letter] -= 1
            letter_count += 1
        
    return player_hand

    # COPY_LETTER_POOL = copy.deepcopy(LETTER_POOL)
    # player_hand_list = []
    # while len(player_hand_list) < 10:
    #     random_letter = random.choice(list(COPY_LETTER_POOL))
    #     # print(COPY_LETTER_POOL[random_letter])
    #     if COPY_LETTER_POOL[random_letter] > 0:
    #         player_hand_list.append(random_letter)
    #         COPY_LETTER_POOL[random_letter] -= 1
    #         print(COPY_LETTER_POOL[random_letter])
    #     else:
    #         continue

print(draw_letters())

def uses_available_letters(word, letter_bank):
    #return a boolean 
    #use for loop to loop through word
    #for each letter in word
    #-->if letter is in letter_bank
    #return true
    #-> else false 
    bool_set = set()
    for letter in word:
        if letter in letter_bank:
            bool_set.add(True)
    else:
        bool_set.add(False)


    result = all(bool_set)
    if result:
        return True
    else:
        return False

def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass
