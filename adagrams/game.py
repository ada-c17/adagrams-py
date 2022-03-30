import random

def draw_letters():
    
    letter_frequency = {
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
    
    letter_pool = []
    hand = []

    for k, v in letter_frequency.items():
        for i in range(v):
            letter_pool.append(k)


    while len(hand) < 10:
        letter = random.choice(letter_pool)
        if hand.count(letter) < letter_frequency[letter]:
            hand.append(letter)

    return hand


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    
    # score each word in word_list using score_word(word)
    # find max score of word
    # if tie for max score of word: 
    # if len(word)==10, that word wins
    # elif len(wordA) == len(wordB), word A wins
    # else: shortest word wins
    # try to allow ties between more than 2 words
    # returns best_word which is a tuple ex: ("word", score)
    best_words = []
    highest_score = 0
    
    for word in word_list:
        word_tuple = (word, score_word(word))
        if word_tuple[1] > highest_score:
            best_words = [word_tuple]
            highest_score = word_tuple[1]
        elif word_tuple[1] == highest_score:
            best_words.append(word_tuple)
    
    # first draft, not sure if happpy with this method (not super elegant), needs refactoring
    # also can't test until wave 3 finished 

    if len(best_words) > 1:
        shortest_length_of_word = 10
        index_of_shortest_word = 0

        for i in range(len(best_words): # iterates over the list
            if len(best_word[i][0]) == 10: # look at "word" part of tuple: ("word", score)
                return best_word[i] # return whole tuple
            elif len(best_word[i][0]) < highest_length_of_word: #look at "word" part of tuple
                shortest_length_of_word = len(best_word[i][0])
                index_of_shortest_word = i
        return best_words[index_of_shortest_word]


    return best_words[0] # in a list of len 1 return tuple


    

