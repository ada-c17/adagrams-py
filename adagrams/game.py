import random

def draw_letters():
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
    letters = []
   
    while len(letters) < 10:
        letter = random.choice(list(LETTER_POOL))
        if LETTER_POOL[letter] == 0:
            continue
        else:
            letters.append(letter)
            LETTER_POOL[letter] -= 1
   
    return letters

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:]
    word = word.upper()
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    word = word.upper()
    score_chart = {
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
    score = 0
    for letter in word:
        score += score_chart[letter]
    
    if len(word) > 6:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    word_and_score = []
    for word in word_list:
        score = score_word(word)
        score_tuple = (word, score)
        word_and_score.append(score_tuple)
    
    word_and_score_dict = {}
    for word, score in word_and_score:
        word_and_score_dict[word] = score

    print(word_and_score_dict)

    highest_score = 0
    best_word = ""
    for word, score in word_and_score_dict.items():
        if highest_score > score:
            highest_score = score
            best_word = word

    


# make a conditional branch for a tie
# if more than one word has 10 letters, return the first one
# if no word has 10 letters, return the smallest, or the first of the smallest length