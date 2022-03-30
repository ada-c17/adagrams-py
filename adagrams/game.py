import random

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

def create_letter_pool_list(LETTER_POOL):
    # helper function
    # make empty letter pool list
    # iterate over dictionary to add each letter to the letter pool list however many times its value says to
    # return letter_pool_list
    letter_pool_list = []
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
            letter_pool_list.append(letter)

    return letter_pool_list

def draw_letters():
    # use rand.randint(range) to get a random number
    # use random number as index to pull letter from copy of pool of letters. 
    # once we have 10 letters, return new list of single letters as hand
    letter_pool_list = create_letter_pool_list(LETTER_POOL)
    current_hand = []
    for i in range(10):
        pool_index = random.randint(0, len(letter_pool_list)-1)
        draw_letter = letter_pool_list[pool_index]
        current_hand.append(draw_letter)
        letter_pool_list.remove(draw_letter)
    return current_hand    

def uses_available_letters(word, letter_bank):
    # make copy of letter_bank that we can change
    bank_copy = letter_bank.copy()
    # loop through word
    for letter in word.upper():
        if letter not in bank_copy:
            return False
        else:
            bank_copy.remove(letter)
    return True


def score_word(word):
    #create a dictionary with these point values
    '''Create a dictionary score_board with key-value pairs 
    that are letter and corresponding value.
    Initialize the result to 0
    Loop through the characters in the word
    Check if the character is in the letter_vals dictionary
    If it is, add the value of the letter to the result
    Return the result'''

    result = 0
    extra_point = [7,8,9,10]
    
    values_dict = {
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


    for letter in word:
        if letter.isalpha():
            result += values_dict[letter.upper()]
        else:
            continue
    if len(word) in extra_point:
        result += 8
    return result




def get_highest_word_score(word_list):
    #["cat", "dog", "goose"]
    # ("goose", 7)
    '''
    prefer word with fewest letters
    prefer the word with the fewest letters...
    -unless one word has 10 letters. 
    -If the top score is tied between multiple words 
    and one is 10 letters long, choose the one with 
    10 letters over the one with fewer tiles
    - If the there are multiple words that are the 
    same score and the same length, pick the first one 
    in the supplied list

    '''

    #####OTHER-OPTION########
    # dict_of_score_words = {}
    # for word in word_list:
    #     each_score = score_word(word)
    #     dict_of_score_words[word] = each_score

    # current_highest_score = dict_of_score_words[word_list[0]]
    # current_highest_word =  word_list[0]
    # for word in dict_of_score_words:
    #     if dict_of_score_words[word] > current_highest_score:
    #         current_highest_score = dict_of_score_words[word]
    #         current_highest_word = word
    #     elif dict_of_score_words[word] == current_highest_score:
    #         if len(word) == 10:
    #             current_highest_score = dict_of_score_words[word]
    #             current_highest_word = word
    #             return (current_highest_word, current_highest_score) 
    #         elif len(word) < len(current_highest_word):
    #             current_highest_score = dict_of_score_words[word]
    #             current_highest_word = word
    # return (current_highest_word, current_highest_score) 
        
    
    