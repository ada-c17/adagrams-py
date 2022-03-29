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
    letter_hand = []
    while len(letter_hand) < 10:
        picked_letter = random.choice(list(available_letters.keys()))
        # check frequency
        if letter_hand.count(picked_letter) < available_letters[picked_letter][0]:
            letter_hand.append(picked_letter)
    return letter_hand    

print(draw_letters())

def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:]
    word_uppercase = word.upper()

    for letter in word_uppercase:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

def score_word(word):
    score = 0
    word_uppercase = word.upper()
    for letter in word_uppercase:
        score += available_letters[letter][1]
    if len(word_uppercase) >= 7:
        score += 8
    return score

# print(score_word("aaaaaax"))

def get_highest_word_score(word_list):
    pass