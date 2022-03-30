import random
import copy

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
    # letters = copy.copy(LETTERS)
    letters = LETTERS.copy()
    # letter_pool = copy.copy(LETTER_POOL)
    letter_pool = LETTER_POOL.copy()
    hand = []
    while len(hand) < 10:
        letter = random.choice(letters)
        for key, value in letter_pool.items():
            if letter == key and value > 0:
                letter_pool[key] -= 1
                hand.append(letter)
    return hand


def uses_available_letters(word, letter_bank):
    # no need to create a copy as we are not modifying the letter bank
    # we ARE touching it, but that's okay!! We're not adding or removing
    # anything to the list. 
    # I was getting a weird KeyError sometimes if I tried to break it in the 
    # playtester (like if I was inputting "HOG" instead of "DOG" if the 
    # letters for "DOG" where only available) after I got all the tests to run 
    # so I put in a try/except to catch it but there is probably a much more
    # elegant solution
    try:
    #converts the input to uppercase
        word = word.upper()
    
    #splits word into a list
        guessed_letters = list(word)

    #so this is for the third test mostly
    #counts the amount of times that each letter appears in each list,
    #and if it's greater than the count of the letters in the letter bank, return False
        letter_count_guessed_letters = {}
        letter_count_letter_bank = {}
    
        count = 0
        for letter in guessed_letters:
            count += 1
            letter_count_guessed_letters[letter] = count

    #reinit count just in case of anything crazy.....
        count = 0
        for letter in letter_bank:
            count += 1
            letter_count_letter_bank[letter] = count
    
    #does the comparison stuff
        for letter, count in letter_count_guessed_letters.items():
            if count > letter_count_letter_bank[letter]:
                return False
            else:
        #all() returns True if all guessed letters are in the letter bank, False if not
        #basically it's saying, hey here's this loop, are we getting True every time
        #if not, we're doing to return False
        #I also had to use a list comprehension, which is t r i c k y
        #I tried to escape using one as they are awful to explain or understand
        #I could not. T_T
        
                uses_letters = all(letter in letter_bank for letter in guessed_letters)
                return uses_letters
    
    except KeyError:
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
    scores = {}
    for word in word_list:
        scored_word = score_word(word)
        scores[word] = scored_word
    highest_scoring_word = max(scores, key=scores.get)
    highest_score = max(scores.values())
    return (highest_scoring_word, highest_score)

# In the case of tie in scores, use these tie-breaking rules:
# prefer the word with the fewest letters...
# ...unless one word has 10 letters. If the top score is tied 
# between multiple words and one is 10 letters long, choose the 
# one with 10 letters over the one with fewer tiles
# If the there are multiple words that are the same score and 
# the same length, pick the first one in the supplied list