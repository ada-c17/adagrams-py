import random

def generate_random_letter(x,y):

    return  chr(random.randint(ord(x),ord(y)))

letters= []
LETTER_POOL = {
    'A' : 9,
    'B' : 2,
    'C' : 2,
    'D' : 4,
    'E' : 12,
    'F' : 2,
    'G' : 3,
    'H' : 2,
    'I' : 9,
    'J' : 1,
    'K' : 1,
    'L' : 4,
    'M' : 2,
    'N' : 6,
    'O' : 8,
    'P' : 2,
    'Q' : 1,
    'R' : 6,
    'S' : 4,
    'T' : 6,
    'U' : 4,
    'V' : 2,
    'W' : 2,
    'X' : 1,
    'Y' : 2,
    'Z' : 1,
}


def draw_letters():
    count = 1
    while count <= 10:
        random_letter = generate_random_letter("A", "Z")
        # generates random letter from a-z
         # compares letter against distribution dictionary
        if LETTER_POOL[random_letter] == 0:
            continue
        else:
            letters.append(random_letter)
            count += 1
            LETTER_POOL[random_letter] -= 1
    return letters




def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass