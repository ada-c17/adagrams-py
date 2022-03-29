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

def draw_letters():
    new_pool = []
    for letter, count in LETTER_POOL.items():
        new_pool.extend([letter] * count)
    
    letters = []
    already_drawn = []
    while len(letters) < 10:
        draw = random.randint(0,len(new_pool)-1)
        if draw not in already_drawn:
            letters.append(new_pool[draw])
            already_drawn.append(draw)

    return letters


def uses_available_letters(word, letter_bank):
    uppercase_word = word.upper()
    bank_copy = list(letter_bank)
    
    for char in uppercase_word:
        if char in bank_copy:
            bank_copy.remove(char)
        else:
            return False
    return True


def score_word(word):
    total_score = 0
    for char in word.upper():
        total_score += score_chart[char]
    if len(word) > 6:
        total_score += 8
    return total_score

def break_tie(word_list):
    shortest = 11
    winner = None
    for word in word_list:
        if len(word) == 10:
            winner = word
            break
        elif len(word) < shortest:
            shortest = len(word)
            winner = word
    
    return winner, score_word(winner)

def get_highest_word_score(word_list):
    top_score = 0
    winners = []
    for word in word_list:
        score = score_word(word)
        if score > top_score:
            top_score = score
            winners = [word]
        elif score == top_score:
            winners.append(word)
    if len(winners) > 1:
        return break_tie(winners)
    return winners[0],top_score