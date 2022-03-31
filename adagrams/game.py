import random

LETTER_POOL = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, 
    "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 8,
    "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1,
    "Y": 2, "Z": 1}
LETTERS = ["A","B","C","D","E","F","G","H","I","J","K","L", "M", "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

SCORE_CHART = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}
def draw_letters():
    # make copy of the letter bank and letter pool constants
    letters = LETTERS.copy()
    letter_pool = LETTER_POOL.copy()
    # initiate hand empty list
    hand = []
    while len(hand) < 10:
        letter = random.choice(letters)
        for key, value in letter_pool.items():
            if letter == key and value > 0:
                letter_pool[key] -= 1
                hand.append(letter)
    return hand


def uses_available_letters(word, letter_bank):
    #converts the input to uppercase
    word = word.upper()
    
    #splits word into a list
    guessed_letters = list(word)

    #make a list of booleans for each letter, if in letter bank, return True
    boolean_list = []
    for letter in guessed_letters:
        if letter in letter_bank:
            boolean_list.append(True)
        else:
            boolean_list.append(False)
    
    #all checks to see if everything in list is truthy
    if all(boolean_list):
    #counts the amount of times that each letter appears in each list,
    #and if it's greater than the count of the letters in the letter bank, return False
        letter_count_guessed_letters = {}
        letter_count_letter_bank = {}
    
        count = 0
        for letter in guessed_letters:
            count += 1
            letter_count_guessed_letters[letter] = count

    #reinit count
        count = 0
        for letter in letter_bank:
            count += 1
            letter_count_letter_bank[letter] = count
    
    # comparison of count of letters in letter bank
        for letter, count in letter_count_guessed_letters.items():
            if count > letter_count_letter_bank[letter]:
                return False
            else:
                return True

    # returns false if the all() function doesn't return True
    else:
        return False
            

def score_word(word):
    # change word to uppercase in case it's not 
    word = word.upper()
    # iterate through each letter in the word, iterate through score chart
    # and use .items to access both the key(points) and value(letters),
    # if letter from word is in the score chart value(letters)
    # add the key(points) to the score
    score = 0
    for letter in word:
        for points, letters in SCORE_CHART.items():
            if letter in letters:
                score += points
    # check length of word to calculate bonus score
    if len(word) >= 7:
        score += 8
    return score


def get_highest_word_score(word_list):
    #make a dictionary of all the scores
    scores = {}
    for word in word_list:
        scored_word = score_word(word)
        scores[word] = scored_word
    #find the highest scoring word and score
    highest_scoring_word = max(scores, key=scores.get)
    highest_score = max(scores.values())
    #make a list of the winning words
    winning_words = []
    for word, score in scores.items():
        if score == highest_score:
            winning_words.append(word)
    #if there's more than one word, in the list, tiebreaker time
    if len(winning_words) > 1:
        for word in winning_words:
            if len(word) == 10:
                return (word, highest_score)
        return (min(winning_words, key=len), highest_score)
    #else just return the highest scoring word
    else:
        return (highest_scoring_word, highest_score)