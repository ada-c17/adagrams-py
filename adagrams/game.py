import random
import copy

# dictionary of letters and their frequencies. Dictionary used for readability and easy to modify.
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
# dictionary of letters and their points values. letters are in tuples for readability
SCORES = {
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K"): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10
}


def draw_letters():
    # build the letter bank
    letter_bank = []
    for letter in LETTER_POOL:
        letter_bank.extend([letter] * LETTER_POOL[letter])
    # shuffle the letter bank
    random.shuffle(letter_bank)
    return letter_bank[:10]


def uses_available_letters(word, letter_bank):
    temp_copy = copy.copy(letter_bank)
    word = word.upper()
    for letter in word:
        if letter in temp_copy:
            temp_copy.remove(letter)
        else:
            return False
    return True


def score_word(word):
    sum = 0
    word = word.upper()
    if len(word) > 6:
        sum += 8
    for letter in word:
        for key in SCORES:
            if letter in key:
                sum += SCORES[key]
                break
    return sum


def get_highest_word_score(word_list):
    score = 0
    best_answer = ""
    for word in word_list:
        if score_word(word) > score:
            score = score_word(word)
            best_answer = word
        elif score_word(word) == score:
            if len(best_answer) == 10:
                pass
            elif len(word) == 10:
                best_answer = word
            elif len(best_answer) > len(word):
                best_answer = word

    return best_answer, score
