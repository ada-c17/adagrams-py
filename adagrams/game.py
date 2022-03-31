import random
import copy
import collections
# from tests.test_wave_03 import SCORE_CHART


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

SCORE_CHART = {
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
    'P': 2, 
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


def generate_random_letter(x,y):
    return chr(random.randint(ord(x),ord(y)))


def draw_letters():
    letters = []
    count = 1
    letter_pool_copy = copy.copy(LETTER_POOL)
    while count <= 10:
        random_letter = generate_random_letter("A", "Z")
        if letter_pool_copy[random_letter] == 0:
            continue
        else:
            letters.append(random_letter)
            count += 1
            letter_pool_copy[random_letter] -= 1
    return letters


def uses_available_letters(word, letters):
    word_freq = collections.Counter(word.upper())
    letters_freq = collections.Counter(letters)
    for letter in word:
        if letter.upper() not in letters:
            return False
    for letter in word_freq:
        if word_freq[letter] > letters_freq[letter]:
            return False
        else:
            return True


def score_word(word):
    cap_word = word.upper()
    total_score = 0
    if word == " ":
        return total_score
    if len(word) >= 7 and len(word) <= 10:
        total_score += 8
    for letter in cap_word:
        total_score += SCORE_CHART[letter]
    return total_score


def get_highest_word_score(words):
    score_dict = build_score_dict(words)
    max_score_word = max(score_dict, key=score_dict.get)
    max_score = score_dict[max_score_word] 
    max_score_words = [word for word in words if score_dict[word] >= max_score]
    if len(max_score_words) == 1:
        return (max_score_word, max_score)
    return resolve_ties(max_score_words, score_dict)


def build_score_dict(words):
    score_dict = {}
    for word in words:
        score_dict[word] = score_word(word)
    return score_dict


def resolve_ties(max_score_words, score_dict):
    word_lengths = build_lengths_dict(max_score_words)
    shortest_word = min(word_lengths, key=word_lengths.get)
    for key, value in word_lengths.items():
        if value == 10:
            return (key, score_dict[key])
        else:
            result = (shortest_word, score_dict[shortest_word])
    return result


def build_lengths_dict(max_score_words):
    word_lengths = {}
    for word in max_score_words:
        word_lengths[word] = len(word)
    return word_lengths