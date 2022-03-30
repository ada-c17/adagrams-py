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
# -----test_wave_01-----------


def draw_letters():
    letter_list = []
    # get all letters and repeats from the pool into a list
    # ex-if letter 'A' has a value of 2: should have ['A','A']
    for letter in LETTER_POOL:
        repeat_num = LETTER_POOL[letter]
        letter_list.extend(letter*repeat_num)
    print(letter_list)

    new_letter_list = []
    count_dict = {}


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
    scores = []
    for word in word_list:
        score = score_word(word)
        scores.append({
            "word": word,
            "score": score
        })
    top_words = []
    for word in scores:
        if word["score"] == max(word["score"] for word in scores):
            top_words.append(word)
    if len(top_words) == 1:
        return top_words[0]["word"], top_words[0]["score"]
    elif len(top_words) < 1:
        return None
    elif len(top_words) > 1:
        top_word_lengths = []
        for word in top_words:
            top_word_lengths.append(len(word["word"]))
        if 10 in top_word_lengths:
            ten_char_word = top_words[top_word_lengths.index(10)]
            return ten_char_word["word"], ten_char_word["score"]
        else:
            min_len_word = top_words[top_word_lengths.index(
                min(top_word_lengths))]
            return min_len_word["word"], min_len_word["score"]
