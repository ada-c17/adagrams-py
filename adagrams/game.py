import random
'''
Importing random module so we can use its .choice() method to randomly select letters from list
'''


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

    num_letters = 0
    while num_letters < 10:
        letter = random.choice(letter_list)
        if letter in count_dict:
            if count_dict[letter] < LETTER_POOL[letter]:
                count_dict[letter] += 1
                new_letter_list.append(letter)
                num_letters += 1
        else:
            count_dict[letter] = 1
            new_letter_list.append(letter)
            num_letters += 1
    return new_letter_list

# -------test_wave_02---------------


def uses_available_letters(word, letter_bank):
    word = word.upper()

    for letter in word:
        keep_checking = True
        if letter in letter_bank:
            letter_count = word.count(letter)
            letter_list_count = letter_bank.count(letter)
            if letter_count <= letter_list_count:
                keep_checking
            else:
                keep_checking = False
                break
        else:
            return False
    return keep_checking

# -----test_wave_03-----------


score_dict = {
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


def score_word(word):
    score_point = 0
    word = word.upper()
    for letter in word:
        score_point += score_dict[letter]
    if len(word) >= 7:
        score_point += 8
    return score_point

# ------test_wave04-------


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
