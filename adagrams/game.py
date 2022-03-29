import random
import string
# from tokenize import blank_re

letters_dict = {
    "A": 9,
    "B": 2,
    "C": 2,
    "D": 4,
    "E": 12,
    "F": 2,
    "G": 3,
    "H": 2,
    "I": 9,
    "J": 1,
    "K": 1,
    "L": 4,
    "M": 2,
    "N": 6,
    "O": 8,
    "P": 2,
    "Q": 1,
    "R": 6,
    "S": 4,
    "T": 6,
    "U": 4,
    "V": 2,
    "W": 2,
    "X": 1,
    "Y": 2,
    "Z": 1
}

score_dict = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}
def draw_letters():
    """
        output: list of 10 strings
        no parameters
        letters should be randomly drawn from a pool of letters
        letters should reflect distribution from a table
        (dictionary, pool_of_letters)
        drawn letters cannot return more than the allotted amount(?)
        once something is drawn, will probably have to subtract from the value of that letter by 1
        if the value is 0, make it no longer accessible
        possibly make list of dicts if random doesnt work?
        random.choice()?

        """
    hand_list = []
    hand_dict = letters_dict.copy()
    while len(hand_list) < 10:
        random_letter = random.choice(string.ascii_uppercase)
        for letter in hand_dict:
            if letter == random_letter:
                if hand_dict[letter] >= 1:
                    hand_list.append(letter)
                    hand_dict[letter] -= 1 
    # print(", ".join(hand_list))  
    return hand_list

def uses_available_letters(word, letter_bank):
    """
    input: word (string), letter_bank: list of drawn letters
    output: True or False
    True if every letter in word is available in letter_bank
    False if not above, or if letter in word that is not present in the letter_bank,
    or if word is longer than letter_bank
    """
    available_letters = letter_bank.copy()
    if len(word) > len(letter_bank):
        return False

    extra_letters = set(word.upper()) - set(letter_bank)
    if extra_letters:
        return False

    for letter in word.upper():
        if not letter in available_letters:
            return False
        else:
            available_letters.remove(letter)
    return True

def score_word(word):
    """
    input: word (string)
    output: integer (number of points scored)
    function will add points assciated w/each letter
    8 bonus points will be awarded if length of word >= 7
    """
    score = 0
    
    if len(word) >= 7:
        score += 8
    for letter in word.upper():
        for key, value in score_dict.items():
            if letter in value:
                score += key

    return score            

def get_highest_word_score(word_list):
    """
    input: list of strings
    output: returns tuple winning_word (string), score (int)
    in case of tie:
    word with fewest letters will win
    if multiple words have same length, winner is first one in list
    exception: in case of tie, if one of the words has len(10),
    that word wins
    """
    # for finding max score
    score_list = []
    tuple_list = []
    for word in word_list:
        word_tuple = word, score_word(word)
        tuple_list.append(word_tuple)
        score_list.append(score_word(word))

    max_score = max(score_list)
    max_index_list = [i for i, score in enumerate(score_list) \
        if score == max_score]

    if len(max_index_list) == 1:
        return word_tuple[max_index_list[0]]
    else:
        for word, score in word_tuple:
            if score == max_score and len(word) == 10:
                return word, score
            else:
                small_word_length = 9
                for index in max_index_list:
                    if len(word) in word_tuple[index] < small_word_length:
                        small_word_length = len(word)
                    if small_word_length == len(word):
                        return word, score