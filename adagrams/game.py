from itertools import repeat
import random 
from collections import Counter

def draw_letters():
    # Returns an array of ten strings - letters should be randomly drawn from a pool of letters
    # Invoking this function should not change the pool of letters

    all_letters = []
    letter_a = all_letters.extend(repeat('A', 9))
    letter_b = all_letters.extend(repeat('B', 2))
    letter_c = all_letters.extend(repeat('C', 2))
    letter_d = all_letters.extend(repeat('D', 4))
    letter_e = all_letters.extend(repeat('E', 12))
    letter_f = all_letters.extend(repeat('F', 2))
    letter_g = all_letters.extend(repeat('G', 3))
    letter_h = all_letters.extend(repeat('H', 2))
    letter_i = all_letters.extend(repeat('I', 9))
    letter_j = all_letters.extend(repeat('J', 1))
    letter_k = all_letters.extend(repeat('K', 1))
    letter_l = all_letters.extend(repeat('L', 4))
    letter_m = all_letters.extend(repeat('M', 2))
    letter_n = all_letters.extend(repeat('N', 6))
    letter_o = all_letters.extend(repeat('O', 8))
    letter_p = all_letters.extend(repeat('P', 2))
    letter_q = all_letters.extend(repeat('Q', 1))
    letter_r = all_letters.extend(repeat('R', 6))
    letter_s = all_letters.extend(repeat('S', 4))
    letter_t = all_letters.extend(repeat('T', 6))
    letter_u = all_letters.extend(repeat('U', 4))
    letter_v = all_letters.extend(repeat('V', 2))
    letter_w = all_letters.extend(repeat('W', 2))
    letter_x = all_letters.extend(repeat('X', 1))
    letter_y = all_letters.extend(repeat('Y', 2))
    letter_z = all_letters.extend(repeat('Z', 1))
    # compare dictionary value assigned to letter to make sure that it isn't going over the original dict value
    output = []

    while len(output) < 10:
        selected_letter = random.choice(all_letters)
        output.append(selected_letter)
        all_letters.remove(selected_letter)

    return output

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass