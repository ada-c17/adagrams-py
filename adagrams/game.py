import random
import copy 
from adagrams.constants import LETTER_POOL

'''
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
'''

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



def score_word(word):
    pass






def get_highest_word_score(word_list):
    pass





