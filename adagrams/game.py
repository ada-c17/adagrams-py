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
        letter_pool.remove(letter)
        hand.append(letter)

    return hand


def uses_available_letters(word, letter_bank):

    letter_bank_copy = copy.deepcopy(letter_bank)
    uppercase_word = word.upper()
    for letter in uppercase_word: 
        if letter not in letter_bank_copy:
            return False
        else: 
            letter_bank_copy.remove(letter)

    return True

    #copy letter bank 
    # loop thru word and delete from letter_bank_copu
    # if not in letter_bank return false 
    
    # returns true if all letters available in letter_bank in right quantities
    # otherwise return false 
    # remember to use .upper()

def score_word(word):
    letter_points = {
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
    total_score = 0 
    uppercase_word = word.upper()
    for letter in uppercase_word: 
        total_score += letter_points[letter]
    
    if len(word) >= 7:
        total_score += 8
    
    return total_score

#word parameter is a string 
#sum points for each letter 
#word len of 7 8 9 or 10 get 8 bonus points
#returns score, which is an integer


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
            elif len(best_word[i][0]) < shortest_length_of_word: #look at "word" part of tuple
                shortest_length_of_word = len(best_word[i][0])
                index_of_shortest_word = i
        return best_words[index_of_shortest_word]


    return best_words[0] # in a list of len 1 return tuple


    

