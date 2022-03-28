import random

def create_letter_pool():

    letter_pool = []

    letter_frequencies = {
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
    'Z': 1}

    for letter in letter_frequencies:

        for i in range(0, letter_frequencies[letter]):

            letter_pool.append(letter)

    return letter_pool


def draw_letters():
    
    letter_pool = create_letter_pool()

    hand = []

    while len(hand) < 10:

        num = random.randint(0, len(letter_pool)-1)
        hand.append(letter_pool[num])
        letter_pool.pop(num)

    return hand

def uses_available_letters(word, letter_bank):
    anagram_attempt = word.upper()
    letters = set(anagram_attempt)

    for letter in letters:
        if letter_bank.count(letter) < anagram_attempt.count(letter):
            #should I print something here so the user knows what they did wrong?
            return False
        elif letter not in letter_bank:
            return False
    
    return True

def score_word(word):

    score_chart = {
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

    score = 0

    for letter in word.upper():
        
        score += score_chart[letter]

    if len(word) >= 7 and len(word) <= 10:

        score += 8

    return score

def get_highest_word_score(word_list):
    pass