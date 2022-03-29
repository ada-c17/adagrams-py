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

def draw_letters():
    import string
    import random
    import copy

    user_hand = []
    temp_dict = copy.deepcopy(LETTER_POOL)

    while len(user_hand) < 10:
        letter = random.choice(string.ascii_uppercase)
        letter_count = temp_dict[letter]
        if letter_count == 0:
            continue
        else:
            temp_dict[letter] -= 1
            user_hand.append(letter)

    return user_hand


def uses_available_letters(word, letter_bank):
    word = word.upper()
    for letter in word:
        letter_count = word.count(letter)
        bank_count = letter_bank.count(letter)
        if letter in letter_bank:
            if letter_count <= bank_count:
                continue 
            else:
                return False
        else: 
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

