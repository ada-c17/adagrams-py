import random 
from collections import Counter

def draw_letters():
    # Returns an array of ten strings - letters should be randomly drawn from a pool of letters
    # Invoking this function should not change the pool of letters

    all_available_letters = {
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

    output = []

    while len(output) < 10:
        letter_frequency = Counter(output)
        print(letter_frequency)
        selected_letter = random.choices(list(all_available_letters.keys()), weights=all_available_letters.values(), k = 1)
        print(selected_letter)
    #     for letter, weight in letter_frequency.items():
    #         if letter in letter_frequency and weight > all_available_letters[letter]:
    #             continue
    #         else:
    #             output.extend(selected_letter)
    # print(output)  
    # return output

    # selected_letters = random.choices(list(all_available_letters.keys()), weights=all_available_letters.values(), k = 10)
    # return selected_letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass