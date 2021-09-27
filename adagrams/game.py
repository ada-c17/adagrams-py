import random

def draw_letters():
    letters = {'A': 9, 'B': 2, 'O': 8, 'C': 2, 'P': 2, 
                    'D': 4, 'Q': 1, 'E': 12, 'R': 6, 'F': 2, 
                    'S': 4, 'G': 3, 'T': 6, 'H': 2, 'U': 4, 
                    'I': 9, 'V': 2, 'J': 1, 'W': 2, 'K': 1, 
                    'X': 1, 'L': 4, 'Y': 2, 'M': 2, 'Z': 1}
    hand = []

    while len(hand) < 10:
        letter = random.choice(list(letters))
        if letters[letter] > 0:
            hand.append(letter)
            letters[letter] -= 1
    return hand


def uses_available_letters(word, letter_bank):
    is_anagram = True
    letters = list(letter_bank)
    
    for letter in word:
        if letter in letters:
            letters.remove(letter)
        else:
            is_anagram = False

    return is_anagram

def score_word(word):
    score = 0
    if len(word) >= 7 and len(word) <= 10:
        score += 8

    word = word.upper()

    for letter in word:
        if letter in "AEIOULNRST":
            score += 1
        elif letter in "DG":
            score += 2
        elif letter in "BCMP":
            score += 3
        elif letter in "FHVWY":
            score += 4
        elif letter == "K":
            score += 5
        elif letter in "JX":
            score += 8
        elif letter in "QZ":
            score += 10

    return score 

    

def get_highest_word_score(word_list):
    highest_score = 0 
    highest_scoring_word = ""
    prev_word = ""

    for word in word_list:
        word_score = score_word(word)

        if word_score > highest_score:
                highest_score = word_score
                highest_scoring_word = word
        elif word_score == highest_score:
            if len(word) < len(highest_scoring_word) and len(highest_scoring_word) != 10:
                highest_score = word_score
                highest_scoring_word = word
            elif len(word) == len(highest_scoring_word) and word_score == highest_score:
                break
            elif len(word) == 10 and word_score == highest_score:
                highest_score = word_score
                highest_scoring_word = word

    return (highest_scoring_word, highest_score)