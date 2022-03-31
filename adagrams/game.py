from random import sample


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


SCORE_DICT = {
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


def draw_letters():
    """Returns a list of 10 random letters from LETTER_POOL"""

    letters = LETTER_POOL.keys()
    frequency = LETTER_POOL.values()
    
    return sample(letters, counts=frequency, k=10)


# Helper function
def get_letter_count(sequence):
    """Returns a dictionary containing the frequency of each character from a sequence"""

    frequency_dict = {}

    for character in sequence:
        frequency_dict[character] = frequency_dict.get(character, 0) + 1

    return frequency_dict


def uses_available_letters(word, letter_bank):
    """Returns True if word uses only letters from letter_bank
    Returns False if word uses letters not from letter_bank"""

    word_count_dict = get_letter_count(word.upper())
    letter_bank = get_letter_count(letter_bank)

    for character, count in word_count_dict.items():
        if count > letter_bank.get(character, 0):
            return False

    return True


def score_word(word):
    """Return the score of a word according to SCORE_DICT mapping"""
    
    if len(word) == 0:
        return 0

    score = 0
    for letter in word.upper():
        if letter in SCORE_DICT:
            score += SCORE_DICT[letter]
    
    # if the length of the word is 7, 8, 9, or 10 
    # then the word gets an additional 8 points
    if len(word) in [7,8,9,10]:
        score += 8
        
    return score


def get_highest_word_score(word_list):
    """Returns a word with the highest score & its score 
    from a list of words.
    """

    highest_score = 0
    highest_score_word = None

    for word in word_list:
        current_score = score_word(word)

        # when a strictly better scored word found
        if current_score > highest_score:
            highest_score = current_score
            highest_score_word = word

        # in case of tie
        elif current_score == highest_score and len(highest_score_word) != 10:
            if len(word) == 10 or len(word) < len(highest_score_word):
                highest_score_word = word

    return highest_score_word, highest_score