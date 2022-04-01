import random
from unittest import TestResult
"""Explain why later"""
import string 
"""Explain why later"""
score_chart = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
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

    # letter_count = len(player_hand) #TAKEN OUT BY JANDE
    # print(letter_count) #TAKEN OUT BY JANDE
    while len(player_hand) < 10:
        # string.ascii_letters #TAKEN OUT BY JANDE
        random_letter = random.choice(string.ascii_uppercase)        
        if LETTER_POOL[random_letter] == 0:
            continue
        else:
            player_hand.append(random_letter)
            LETTER_POOL[random_letter] -= 1
            # letter_count += 1 #TAKEN OUT BY JANDE
        
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

# print(draw_letters())

def uses_available_letters(word, letter_bank):
    #return a boolean 
    #use for loop to loop through word
    #for each letter in word
    #-->if letter is in letter_bank
    #return true
    #-> else false
    # uppercase_word = word.upper() # TAKEN OUT BY JANDE
    list_of_letters = letter_bank[:]
    bool_set = set()
    for letter in word.upper(): # removed variable and replaced with upper method
        if letter in list_of_letters:
            bool_set.add(True)
            list_of_letters.remove(letter)
        else:
            bool_set.add(False)


    # result = all(bool_set) # TAKEN OUT BY JANDE
    if bool_set == {True}: # Realized if we check if bool_set == {True} we can get rid of the variable
        return True
    else:
        return False

def score_word(word):
    # score = 0
    # find the letters in word in the dictionary values
        # for letter in word
        # score += dictionary[letter]
    # if the len(word) >= 7 and 
        # score += 8
    #return score
    score = 0
    for letter in word:
        score += score_chart[letter.upper()]
    if len(word) >= 7:
        score += 8
    return score


word_list = ["AAAAAAAAAA", "BBBBBB"]

def get_highest_word_score(word_list):
<<<<<<< HEAD
    highest_score = 0
    winning_word = ""

    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            winning_word = word
            highest_score = score
        elif score == highest_score:
            if len(winning_word) == 10:
                continue
            elif len(word) == 10:
                winning_word = word
            elif len(word) < len(winning_word):
                winning_word = word
    return (winning_word, highest_score)

    
    # print(f"{score=}")


    # # ***Attempt 1***
    # score = []
    # highest_score = 0
    # for word in word_list:
    #     tuple = (word,score_word(word))
    #     score.append(tuple)
    #     if score_word(word) > highest_score:
    #         highest_score = score_word(word)

    # highest_pairs = score[:]
    # best_words = []
    # for item in score:
    #     if item[1] < highest_score:
    #         highest_pairs.remove(item)
    #     else:
    #         best_words = item[0]

    # for item in highest_pairs:
    #     if len(item[0]) < len(best_words[0]):
    #         highest_word = item

    # print(f"{score=}")
    # print(f"{highest_score=}")
    # print(f"{highest_pairs=}")
    # print(f"{best_words=}")
    # return highest_pairs[0]
=======
    # create empty tuple
    # list_of_tuples = [("DOG", 5), ("BANANA", 10)]
    # max_score = 0
    # winner_word = ""
    # for word in word_list
        # implament score_word(word) to get the score
        # if score >= max_score
            # if len(word) == 10 
            # if len(word)< winner_word
     #now that we have a max_score and a winner_word
    #check if any other word shares the same max_score
    #if so, check if the length of word is 10
    #--> if length is 10, that is the new winner 
    #--> if not, (else) check if length is shorter than current_winner word
                            #--> if so, this will be the new winner_word 
    score_list = []
    max_score = 0
    winning_word = ""
    for i in range(len(word_list)):
        score = score_word(word_list[i])
        tup = (word_list[i], score)
        score_list.append(tup)
        if score > max_score:
            max_score = score
            winning_word = word_list[i]
        winner = (winning_word, max_score)

    for item in score_list:
        if item[1] == max_score and len(item[0]) == 10:
            winner = item
            return winner
        elif item[1] == max_score and len(item[0]) < len(winning_word):
            winner = item

    return winner

print(get_highest_word_score(word_list))
>>>>>>> 3576969174aad1b6bb220e89ff982c7123cff0d2
