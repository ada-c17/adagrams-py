
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
SCORE_CHART = {
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
    user_pool = copy.deepcopy(LETTER_POOL)
    letter_bank = [] 
    while len(letter_bank)< 10: 
        draw = random.choice(list(user_pool))
        for letter in user_pool.keys():
            if user_pool[letter] == 0:
                continue 
            if letter == draw: 
                letter_bank.append(draw) 
                user_pool[letter] -= 1 
                
    return letter_bank 

from collections import Counter 

def uses_available_letters(word, letter_bank):
    input_word = word.upper()
    print(f"This is the value of {input_word=}")
    # word_counter = Counter(input_word)   
    # print(f"Thisis the data type of word_counter: {type(word_counter)=}")
    # print(f"This is the value of {word_counter=}")
    # # letter_bank_counter = Counter(letter_bank)    
    # print(f"This is the value of letter_bank_counter: {letter_bank_counter}")
 
    for letter in input_word:  
        if letter not in letter_bank:
            return False
        elif letter in letter_bank:
            word_letter_frequency = input_word.count(letter)
            letter_bank_frequency = letter_bank.count(letter)
            if word_letter_frequency > letter_bank_frequency:
                return False       
    return True

    # for (k, v), (k2, v2)  in  zip(word_counter.items(), letter_bank_counter.items()): 
    #     zip(word_counter.items(), letter_bank_counter.items()) 
    #     if k == k2 and v > v2: 
    #         return False
    #      
    # return True 
"""
Wave 3: score_word
Now you need a function returns the score of a given word as defined by the Adagrams game.

Implement the function score_word in game.py. This method should have the following properties:

Has one parameter: word, which is a string of characters
Returns an integer representing the number of points
Each letter within word has a point value. The number of points of each letter is summed up to represent the total score of word
Each letter's point value is described in the table below
If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points

"""
def score_word(word):
    input_word = word.upper()
    word_score = 0
    word_length = len(input_word)

    if input_word == "":
        return 0
    if word_length >= 7: 
        word_score = 8
    for letter in input_word:
        word_score += SCORE_CHART[letter]
      
    return word_score
    

def get_highest_word_score(word_list):
    """
    --for loop iterating word in word_list:
        -- if word_score > highest_word_score
            highest_score = (word, score)
        --if word_score == highest_word_score
            
            if word_length == 10
            highest_score = (word, score)

            elif word_length == highest_word_length
            for word in word_list:
                word_length = len(word)
                
    """

    word_list_scores = []
    highest_score = 0
    best_words = []

    

    for word in word_list:
        # word_length= len(word)
        word_score = score_word(word)
        word_list_scores.append(word_score)
        highest_score = max(word_list_scores)
        if word_score == highest_score: 
            best_words.append(word)

    if len(best_words) == 1: 
        word = best_words[0]
        highest_score_tuple = (word, highest_score)
        return highest_score_tuple

    for word in best_words: 
        
        if len(word) == 10: 
            highest_score_tuple = (word, highest_score)
        else: 
            ### this isn't the right way to do it! 
            ## but thought is that we have a 
            shortest_word = min(word_list, key=lambda word: len(word))
            highest_score_tuple = (shortest_word, highest_score)

        



    # for word_score in word_list_scores: 
    #     word_score_frequency = word_list_scores.count(word_score)
    #     highest_score = max(word_list_scores)
    #     print(f"THIS IS THE WORD SCORE FREQUENCY{word_score_frequency=}")
    #     if word_score == highest_score: 
    #         highest_score = word_score
    #         highest_score_tuple = (word, highest_score)
    #         if word_score_frequency > 1: 
    #             if word_length == 10:
                    
    #                 highest_score_tuple = (word, highest_score)
    #             else: 
    #                 shortest_word = min(word_list, key=lambda word: len(word))
    #                 highest_score_tuple = (shortest_word, highest_score)

                    
                    
    return highest_score_tuple
                
                # highest_score.append(word_score)
            # if word_score > highest_word_score: 

        

        # score = score_word(word)
        # score_list.append(score)
        # highest_score = max(score_list)
        # for score in score_list: 
        #     if score == highest_score: 
        #         highest_scores.append(score)
        #         print(f' THIS SHOULD BE A LIST OF TUPLES{highest_scores=}')

    


    #     # score_list.append(score)
    #     #[a word, 3 another,6,10,4,10]
    # highest_score = highest_score.append(word, score)
    # best_score = highest_score[0]
    # for word_info in highest_score:
    #     if word_info[1] > best_score[1]: 



    #     max_score = max(score_list)
    #     if score == max_score: 
    #         best_score.append(word, score)
    #     if len(best_score) > 1: 


    # user_scores = (word, score)
    # score_list.append(user_scores)
    
    # max_score = max(score_list)
    # for user in score_list: 
    #     if user[1] > max_score: 
    #         user[1] = max_score
 
        
# def get_highest_scoring_words(word_list): 
#     best_score = 0
#     score_list = []
#     best_words = []
#     word_lengths = []
#     shortest_words = []

#     for word in word_list: 
#         word_lengths.append(len(word))
#         smallest_length = min(word_lengths)
#         if len(word) == smallest_length:
#             shortest_words.append(word)


#     for word in word_list: 
#         score = score_word(word)
#         score_list.append(score)
#         best_score = max(score_list)
#         if score == best_score: 
#             best_words.append(word)

#     return tuple(best_words, best_score, shortest_words[0]) 

        
    

# def get_highest_word_score(word_list):
#     calculate_score = get_highest_scoring_words(word_list)
#     score = calculate_score[1] 
#     winning_words = calculate_score[0]
#     shortest_word = calculate_score[2]
#     winning_word = ''

#     if len(winning_words) == 1: 
#         winning_word = winning_words[0]
  
#     for word in winning_words: 
#         if len(word) == 10: 
#             winning_word = word
#             break
#         else: 
#             winning_word = shortest_word 
    
#     return tuple(winning_word, score)
    















    



    """
Wave 4: get_highest_word_score
After several hands have been drawn, words have been submitted, checked, scored, and played, 
you need a way to find the highest scoring word. 

This function looks at the list of word_list and calculates which of these words has the highest 
score, applies any tie-breaking logic, and returns the winning word in a special data structure.

Implement a function called get_highest_word_score in game.py. 

This method should have the following properties:

Has one parameter: word_list, which is a list of strings
Returns a tuple that represents the data of a winning word and it's score. 

The tuple must contain the following elements:
index 0 ([0]): a string of a word
index 1 ([1]): the score of that word
In the case of tie in scores, use these tie-breaking rules:
prefer the word with the fewest letters...
...unless one word has 10 letters. 
If the top score is tied between multiple words and one is 10 letters long, 
choose the one with 10 letters over the one with fewer tiles
If the there are multiple words that are the same score and the same length, 
pick the first one in the supplied list"""



