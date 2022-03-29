def draw_letters():
    pass


def uses_available_letters(word, letter_bank):
    letters_valid = True
    letter_bank_copy = []
    for letter in letter_bank:
        letter_bank_copy.append(letter.upper())
    for letter in word:
        letter = letter.upper()
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            letters_valid = False
    return letters_valid


def score_word(word):

    points_dict = {}
    for letter in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]:
        points_dict[letter] = 1
    for letter in ["D", "G"]:
        points_dict[letter] = 2
    for letter in ["B", "C", "M", "P"]:
        points_dict[letter] = 3
    for letter in ["F", "H", "V", "W", "Y"]:
        points_dict[letter] = 4
    for letter in ["K"]:
        points_dict[letter] = 5
    for letter in ["J", "X"]:
        points_dict[letter] = 8
    for letter in ["Q", "Z"]:
        points_dict[letter] = 10

    score = 0

    for char in word.upper():
        if char not in points_dict:
            continue
        else:
            score += points_dict[char]
    if len(word) in range(7, 11):
        score += 8

    return score


def get_highest_word_score(word_list):
    pass
