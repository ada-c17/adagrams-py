import random
def draw_letters():

    letters = ['A','A','A','A','A','A','A','A','A','B','B','C','C','D','D','D','D','E','E','E','E','E','E','E','E','E','E','E','E','F','F','G','G','G','H','H','I','I','I','I','I','I','I','I','I','J','K','L','L','L','L','M','M','N','N','N','N','N','N','O','O','O','O','O','O','O','O','P','P','Q','R','R','R','R','R','R','S','S','S','S','T','T','T','T','T','T','U','U','U','U','V','V','W','W','X','Y','Y','Z']
    
    return random.sample(letters, 10)


def uses_available_letters(word, letter_bank):
    letter_copy = letter_bank[:]
    for i in range(len(word)):
        letter = word[i]
        if letter.islower():
            letter = letter.upper()
        if letter in letter_copy:
            letter_copy.remove(letter)
        else:
            return False
    return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass