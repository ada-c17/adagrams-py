import random
import copy 
from adagrams.constants import LETTER_POOL, LETTER_SCORE_DICT

def draw_letters():
    '''
    input: none
    output: return list of 10 strings, 1 letter each
    frequency of each letter cannot exceed the value of 
    each letter in the LETTER_POOL
    '''
    hand = []
    letter_freq = {}
    
    while len(hand) < 10:
        random_letter = random.choice(list(LETTER_POOL))
        if random_letter in letter_freq:
            if letter_freq[random_letter] < LETTER_POOL[random_letter]:
                letter_freq[random_letter] += 1
                hand.append(random_letter)
        else:
            letter_freq[random_letter] = 1
            hand.append(random_letter)
    return(hand)
        

def uses_available_letters(word, hand):
    '''
    input: word (a string) and hand (a list of strings, one char each)
    output: Returns True if each char is uniquely in hand. Returns
    False otherwise or if char in word is not in hand.
    '''
    word = word.upper()
    hand_copy = copy.deepcopy(hand)
    for letter in word:
        if letter in hand_copy:
            hand_copy.remove(letter)
        elif letter not in hand_copy:
            return False
    return True


def score_word(word):
    '''
    input: word (a string of characters)
    output: Returns a total score based on the value of each char in
    word, as defined in LETTER_SCORE_DICT. Words between 7 and 10 
    char score an extra 8 points.
    '''
    score = 0
    word = word.upper()
    for letter in word:
        for key, value in LETTER_SCORE_DICT.items():
            if letter in value:
                score += key 
    if 7 <= len(word) <= 10:
        score += 8
    return score


def get_highest_word_score(word_list):  
    '''
    input: list of strings representing each word user has created
    output: returns tuple with highest scoring word and score. If tied: 
    shortest length word is preferred, unless length is 10 char
    '''      
    played_word_dict = {}
    for word in word_list:
        score = score_word(word)
        played_word_dict[word] = score

    highest_score = max(played_word_dict.values())
    best_word_list = [key for key, value in played_word_dict.items()\
        if value == highest_score]

    if len(best_word_list) > 1:
        for word in best_word_list:
            if len(word) == 10:
                return word, highest_score
    return min(best_word_list, key=len), highest_score