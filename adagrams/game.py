import random
import copy

LETTER_VALS = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1,
        'S': 1, 'T': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

def draw_letters():
    letter_pool = ['A'] * 9 + ['B'] * 2 + ['C'] * 2 + ['D'] * 4 + ['E'] * 12 + ['F'] * 2\
    + ['G'] * 3 + ['H'] * 2 + ['I'] * 9 + ['J'] * 1 + ['K'] * 1 + ['L'] * 4 + ['M'] * 2\
    + ['N'] * 6 + ['O'] * 8 + ['P'] * 2 + ['Q'] * 1 + ['R'] * 6 + ['S'] * 4 + ['T'] * 6\
    + ['U'] * 4 + ['V'] * 2 + ['W'] * 2 + ['X'] * 1 + ['Y'] * 2 + ['Z'] * 1

    return random.sample(letter_pool, 10)


def convert_word_to_upper(word):
    """
    converts all the letters of a word to upper case
    """
    upper_word = ""
    for letter in word:
        if letter.isalpha(): 
            upper_word += letter.upper()
    return upper_word

def uses_available_letters(word, letter_bank):
    upper_word = convert_word_to_upper(word)
    letter_bank_copy = copy.deepcopy(letter_bank)
    for letter in upper_word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    # Initialize the result to 0
    result = 0

    # Loop through the characters in the word
    for character in word.upper(): 
        # Check if the character is in the LETTER_VALS dictionary
        if character in LETTER_VALS: 
            # Add the value of the letter to the result
            result += LETTER_VALS[character]

    # If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
    if len(word) in range(7, 11):
        result += 8

    # Return the result
    return result
    

def get_highest_word_score(word_list):
    highest_score = 0
    winning_word = ''
    for word in word_list:
        word_score = score_word(word)
        if highest_score < word_score:
            highest_score = word_score
            winning_word = word
        elif highest_score == word_score and len(word) == 10 and len(winning_word) != 10: 
            winning_word = word
        elif highest_score == word_score and len(word) < len(winning_word) and len(winning_word) != 10:
            winning_word = word

    return (winning_word, highest_score)

    # Shortest way would be probably max(list, key=f), however, alot less readable 
    # Also the tie-breaking logic would be harder to implement 