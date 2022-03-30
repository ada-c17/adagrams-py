import random
import copy 
from adagrams.constants import LETTER_POOL, LETTER_SCORE_DICT

# draw a letter, from the letter pool
# put each letter in a dictionary, assign a count
# check if count exceeds the allowed count in the LETTER_POOL
# if the letter is good, append it to hand
# repeat until 10 letters

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
        

# iterate over each letter in the word
# check if letter is in the hand
# if letter is in the hand remove a copy of that letter from the hand
# if letter is not in the hand return False
# move to the next letter

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


# assert score_word("A") == 1
# assert score_word("DOG") == 5
# assert score_word("WHIMSY") == 17

# make score = 0
# iterate over each letter in the word
# find the score of each letter in the score dictionary
#  If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
# add the score of the letter to the existing score
# return score

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
    pass





