"""WAVE 4  Old Code Review """

""" Everything below is from the previous version that got us to 4 passed tests. """       
    # for word in word_list:
    #     # word_length= len(word)
    #     word_score = score_word(word)
    #     word_list_scores.append(word_score)
    #     highest_score = max(word_list_scores)
    #     if word_score == highest_score: 
    #         best_word.append(word)
            

"""
In the case of tie in scores, use these tie-breaking rules:
prefer the word with the fewest letters...
...unless one word has 10 letters. 
"""
    # if len(best_word) == 1: 
    #     word = best_word[0]
    #     highest_score_tuple = (word, highest_score)
    #     return highest_score_tuple


"""
If the top score is tied between multiple words and one is 10 letters long, 
choose the one with 10 letters over the one with fewer tiles
If the there are multiple words that are the same score and the same length, 
pick the first one in the supplied list"""

    # for word in best_word: 
        
    #     if len(word) == 10: 
    #         highest_score_tuple = (word, highest_score)
    #         return highest_score_tuple
    #     else: 
    #         ### this isn't the right way to do it! 
    #         ## but thought is that we have a 
    #         shortest_word = min(word_list, key=lambda word: len(word))
    #         highest_score_tuple = (shortest_word, highest_score)        
                    
    # return highest_score_tuple







"""
    Super old Wave 4 code. Ignore  below """



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
    
