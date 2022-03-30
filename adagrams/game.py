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
    letter_vals = {
        "a": 1, 
        "b": 3, 
        "c": 3, 
        "d": 2, 
        "e": 1, 
        "f": 4, 
        "g": 2, 
        "h": 4, 
        "i": 1, 
        "j": 8, 
        "k": 5, 
        "l": 1, 
        "m": 3, 
        "n": 1, 
        "o": 1, 
        "p": 3, 
        "q": 10, 
        "r": 1, 
        "s": 1, 
        "t": 1, 
        "u": 1, 
        "v": 4, 
        "w": 4, 
        "x": 8, 
        "y": 4, 
        "z": 10 }

    final_score = 0
    letter_count = 0
    length = len(word)

    word = word.lower()

    for char in word:
        letter_count = letter_vals[char]
        final_score += letter_count

    if 7 <= length <= 10:
        final_score += 8   

    return final_score

def get_highest_word_score(word_list):
    word_score = 0
    max_score = [["", 0]]
    score_tuple = tuple() # turn to tuple for [] for score in range(word_list)

    for word in word_list:
        word_score = score_word(word)
        if word_score > max_score[0][1]:
            max_score.clear()
            max_score.append([word, word_score])
        elif word_score == max_score[0][1]:
            max_score.append([word, word_score])
        else:
            continue
        
    if len(max_score) > 1:
        

    score_tuple = tuple(max_score)
    print(score_tuple)
    return score_tuple



word_list = ["AAAAAAAAAA",
"EEEEEEEEEE",
"BBBBBB", 
"WWW", 
"SQUID",
"XX", 
"X"
]

get_highest_word_score(word_list)