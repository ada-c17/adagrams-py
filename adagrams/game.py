import random 

available_letters = {
    'A': [9, 1],
    'B': [2,3], 
    'C': [2, 3], 
    'D': [4, 2], 
    'E': [12, 1], 
    'F': [2, 4], 
    'G': [3, 2], 
    'H': [2, 4], 
    'I': [9, 1], 
    'J': [1, 8], 
    'K': [1, 5], 
    'L': [4, 1], 
    'M': [2, 3], 
    'N': [6, 1], 
    'O': [8, 1], 
    'P': [2,3], 
    'Q': [1,10], 
    'R': [6,1], 
    'S': [4,1], 
    'T': [6,1], 
    'U': [4,1], 
    'V': [2,4], 
    'W': [2,4], 
    'X': [1,8], 
    'Y': [2,4], 
    'Z': [1,10]
}
def draw_letters():
    """Draws a hand of 10 letters"""
    
    letter_hand = []

    while len(letter_hand) < 10:
        picked_letter = random.choice(list(available_letters.keys()))
        # check that letter hasn't exceeded available letter count
        if letter_hand.count(picked_letter) < available_letters[picked_letter][0]:
            letter_hand.append(picked_letter)
    
    return letter_hand    


def uses_available_letters(word, letter_bank):
    """Checks that word can be made with letters in letter_bank"""
    letter_bank_copy = letter_bank[:]

    for letter in word.upper():
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True


def score_word(word):
    """Adds up score for each letter in word and returns total score"""
    score = 0

    for letter in word.upper():
        score += available_letters[letter][1]
    
    if len(word) >= 7:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    """Returns the winning word and top score"""
    scores = []
    top_scoring_words = []

    for word in word_list:
        word_score = score_word(word)
        scores.append(word_score)
    
    max_score = max(scores)

    #makes list of all words with the top score
    for i in range(len(scores)):
        if scores[i] == max_score:
            top_scoring_words.append(word_list[i])

    longest_word = max(top_scoring_words, key=len)
    
    if len(longest_word) == 10:
        return [longest_word, max_score]
    else:
        #finds shortest word with top score
        top_word = min(top_scoring_words, key=len)
        return [top_word, max_score]
