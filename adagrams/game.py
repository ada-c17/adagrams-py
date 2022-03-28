def draw_letters():
    pass


def uses_available_letters(word, letter_bank):
    letters_valid = True
    letter_bank_copy = []
    for letter in letter_bank:
        letter_bank_copy.append(letter.lower())
    for letter in word:
        letter = letter.lower()
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            letters_valid = False
    return letters_valid


def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass
