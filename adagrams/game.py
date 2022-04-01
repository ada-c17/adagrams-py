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

LETTER_SCORE = {
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

    user_letters = []
    copy_letter_pool = dict(LETTER_POOL)
    print(copy_letter_pool)
    while len(user_letters) < 10:
        random_letter = random.choice(list(copy_letter_pool.keys()))
        user_letters.append(random_letter)
        copy_letter_pool.update({random_letter:copy_letter_pool[random_letter] - 1}) # Reduce value of letter by 1
        if copy_letter_pool[random_letter] == 0: # Delete any letter from dict with value of 0
            del copy_letter_pool[random_letter]

    return user_letters


def uses_available_letters(word, letter_bank):
    aCopy = list(letter_bank)
    for letter in word:
        if letter.upper() in aCopy:
            aCopy.remove(letter.upper())
        else:
            return False
    return True


def score_word(word):
    score = 0
    for letter in word.upper():
      score += LETTER_SCORE[letter]
    if len(word) >= 7:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    highestScore = 0
    winningWord = ""
  
    for word in word_list:
        if score_word(word) > highestScore:
            highestScore = score_word(word)
            winningWord = word
    
        elif score_word(word) == highestScore:
            if len(word) == 10 and len(winningWord) != 10:
                winningWord = word
            if len(word) < len(winningWord) and len(winningWord) == 10:
                winningWord != word
            elif len(word) < len(winningWord):
                winningWord = word
        
    return (winningWord, highestScore)



