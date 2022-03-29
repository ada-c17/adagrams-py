import random

def draw_letters():
    letter_pool =["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", "C", "D", "D", "D", "D", \
        "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "F", "F", "G", "G", "G", "H", "H", \
        "I", "I", "I", "I", "I", "I", "I", "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", \
        "N", "N", "N", "N", "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", "P", "Q", "R", \
        "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", "T", "T", "T", "T", "U", \
        "U", "U", "U", "V", "V", "W", "W", "X", "Y", "Y", "Z"]
    
    letter_bank = []

    letter_bank = random.sample(letter_pool, 10)
    
    return letter_bank

def uses_available_letters(word, letter_bank):
    is_valid = False
    user_input_list = []
    word = word.upper()
    for letter in word:
        user_input_list.append(letter)
    for element in user_input_list:
        if element in letter_bank:
            if user_input_list.count(element) <= letter_bank.count(element):
                is_valid = True
        else:
            is_valid = False
    return is_valid


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

# print(uses_available_letters("DOG", ["D", "O", "C", "D", "E", "F", "X", "H", "I", "J"]))