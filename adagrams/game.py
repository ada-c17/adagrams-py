import random 
available_letters = {
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
    letter_hand = []
    while len(letter_hand) < 10:
        picked_letter = random.choice(list(available_letters.keys()))
        # check frequency
        if letter_hand.count(picked_letter) < available_letters[picked_letter]:
            letter_hand.append(picked_letter)
    return letter_hand    

print(draw_letters())

def uses_available_letters(word, letter_bank):
    # create a copy of letter_bank
    # for letter in word, if letter in letter_bank:
    # remove letter from letter_bank
    # else: return false
    # return True
    letter_bank_copy = letter_bank[:]
    word_uppercase = word.upper()

    for letter in word_uppercase:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

# print(uses_available_letters("FED",['E', 'J', 'D', 'W', 'S', 'L', 'C', 'W', 'D', 'F']))
# print(uses_available_letters("feD",['E', 'J', 'D', 'W', 'S', 'L', 'C', 'W', 'D', 'F']))

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass