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

    points_dict = {}
    for letter in ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]:
        points_dict[letter] = 1
    for letter in ["d", "g"]:
        points_dict[letter] = 2
    for letter in ["b", "c", "m", "p"]:
        points_dict[letter] = 3
    for letter in ["f", "h", "v", "w", "y"]:
        points_dict[letter] = 4
    for letter in ["k"]:
        points_dict[letter] = 5
    for letter in ["j", "x"]:
        points_dict[letter] = 8
    for letter in ["q", "z"]:
        points_dict[letter] = 10

    score = 0

    for char in word.lower():
        if char not in points_dict:
            continue
        else:
            score += points_dict[char]
    if len(word) in range(7, 11):
        score += 8

    return score


def get_highest_word_score(word_list):
    pass
