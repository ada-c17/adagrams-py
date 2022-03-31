from random import shuffle
from collections import Counter

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

POINT_SCALE = {
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
    'Z': 10}

def draw_letters():
    letters = []
    # Create a new list of all the elements of letter pool by their count
    letter_bag = list(Counter(LETTER_POOL).elements())
    # Randomly reorganize the letters in letter_bag
    shuffle(letter_bag)

    while len(letters) < 10: 
        letters.append(letter_bag.pop())
    
    return letters


def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank.copy()
    for letter in word.upper():
        if letter not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter)
    return True


def score_word(word):
    total = 0
    for letter in word:
        total += POINT_SCALE[letter.upper()]
    if len(word) >= 7:
        total += 8
    return total


def get_highest_word_score(word_list):
    word_scores = {}
    top_words = []
    # Create a dictionary of the words from word_list and their scores 
    for word in word_list:
        word_scores[word] = score_word(word)

    highest_score = max(word_scores.values())
    
    for word in word_scores:
        if word_scores[word] == highest_score:
            top_words.append(word)

    shortest_word = min(top_words, key=len)  
    # Sorts our dictionary of the words and their score by the words length,
    # in descending order
    sorted_scores = sorted(word_scores, key=len, reverse=True)
    
    for word in sorted_scores:
        if word in top_words:
            if len(word) == 10:
                return tuple((word, word_scores[word]))
            elif word == shortest_word:
                return tuple((word, word_scores[word]))


