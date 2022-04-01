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

LETTER_POINT ={
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K"): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10
}


def draw_letters():
    """Drawing 10 letters from a pool of letter and return a list of that letters"""
    # a list to store all letters from a pool of letter
    list_letter = []
    # loop over LETTER_POOL to get key and value
    # key will be the letter adding to list and 
    # value is number of times that the letter will be adding
    for letter, count in LETTER_POOL.items():
        # adding letter into list depend on value of count 
        for i in range(count):
            list_letter.append(letter)
    # create a list that randomly draw 10 letters from list_letter 
    letter_draw = random.sample(list_letter, k=10)
    
    return letter_draw


def uses_available_letters(word, letter_bank):
    """
    Checking each letter of word:
        - return False if it is not in letter_bank
        - return True if it is in letter_banks
    """
    # create a new list which same as letter_bank, so it doen't effect to original when editing
    letter_bank_copy = letter_bank.copy()
    # loop over word to get each character
    for char in word.upper():
        # return False if the character of word not in the new created list
        if char not in letter_bank_copy:
            return False
        # otherwise removing each character of word from letter_bank_copy when it is in there
        # return True after removing all characters of word that is in letter_bank_copy
        else: 
            letter_bank_copy.remove(char)
    return True


def score_word(word):
    """
    Sum score of each character of input
        - return 0 if input is empty, integer, float, or characters of number.
        - otherwise,sum point if the character of input is uppercase or lowercase and it is in table of point value
        - if input has special character then ignore that special character
        - return total score at the end
    """
    # create a variable to sum score for all valid input
    total_score = 0
    # return 0 if input is empty or not string
    if (len(word) == 0) or (type(word) != str):
        return 0

    # loop over char_point dictionary to get key and value for comparing
    for letter, point in LETTER_POINT.items():
        # loop over the word to get each character and check whether is it in the key of char_point
        for char in word:
            # get point value from char_point dictionary to sum if character of word is string and it is in tuple key of dictionary
            if char.upper() in letter:
                total_score += point

    # if length of word is from 7 to 10, add additional 8 point
    if len(word) > 6 and len(word) < 11:
        total_score += 8
    return total_score


def get_highest_word_score(word_list):
    """Finding higest score and return the word and score in Tuple."""

    # find max score
    max_score = max([score_word(word) for word in word_list])

    # find best scoring words
    best_scoring_words = [word for word in word_list if max_score == score_word(word)]

    # if there are no ties, return best scoring word and max score
    if len(best_scoring_words) == 1:
        best_scoring_word = best_scoring_words[0]
        return (best_scoring_word, max_score)

    # If there is a tie and at least one of the words is ten letters, return the first word with ten letters.
    for word in best_scoring_words:
        if len(word) == 10:
            best_scoring_word = word
            return (best_scoring_word, max_score)

    # If there is a tie and no words are ten letters long, then return the shortest word.
    smallest_length = min([len(word) for word in best_scoring_words])
    for word in best_scoring_words:
        if len(word) == smallest_length:
            best_scoring_word = word
            return (best_scoring_word, max_score)
