
import random
import copy 

letter_pool = {
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
    user_pool = copy.deepcopy(letter_pool)
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

    word = word.upper()

    input_word = word.upper()
    word_counter = Counter(input_word)
    letter_bank_counter = Counter(letter_bank)
    
    for letter in input_word: 
        if letter not in letter_bank:
            return False 
        
    for (k,v), (k2,v2)  in  zip(word_counter.items(), letter_bank_counter.items()): 
        if k == k2 and v <= v2: 
            return True
        else: 
            return False 

            word = word.upper()

            letter_bank = draw_letters()
            return TRUE or FALSE 

            ## make sure that case doesn't matter for word input 
            ## do not change the letter_bank (no remove from list! only compare to list)

            for letter in word: 
                if letter not in letter_bank: 
                    return FALSE
                else: 
                    if letter in letter_bank: 
                        if word has same letter more than once, letter_bank must also!: 
    pass

    """
Wave 2: use_available_letters
Next, you need a way to check if an input word (a word a player submits) only uses 
characters that are contained within a collection (or hand) of drawn letters. 
Essentially, you need a way to check if the word is an anagram of some or all of 
the given letters in the hand.

To do so, implement the function called uses_available_letters in game.py. 
This function should have the following properties:

Has two parameters:
word, the first parameter, describes some input word, and is a string
letter_bank, the second parameter, describes an array of drawn letters in a hand. 
You can expect this to be an array of ten strings, with each string representing a letter
Returns either True or False
Returns True if every letter in the input word is available (in the right quantities) in the letter_bank
Returns False if not; if there is a letter in input that is not present in the 
letter_bank or has too much of compared to the letter_bank."""


def score_word(word):
    pass
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
    

def get_highest_word_score(word_list):
    pass
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
    