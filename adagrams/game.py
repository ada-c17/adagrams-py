
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


score_chart = {
    1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2 : ["D", "G"],
    3 : ["B", "C", "M", "P"],
    4 : ["F", "H", "V", "W", "Y"],
    5 : ["K"],
    8 : ["J", "X"],
    10: ["Q", "Z"],
}


# result = random.choice(list(LETTER_POOL))
# print(result)


# result_2 = random.sample((list(LETTER_POOL)), 10)
# print(result_2)


def draw_letters():
    """
    import random
    ten_letters = [] 

    * sytax for random module with dict: random.choice(list(LETTER_POOL))
    drawing process:
    for loop:
        >assign randomly picked letter to variable selection
        selection = random.choice(list(LETTER_POOL))
        >if selection in LTTTER_POOL, LETTER_POOL[selection] -= 1
            >if LETTER_POOL[selection] < 1, remove it(need deepcopy of dict)
            > ten_letters.append
    """
    ten_letters = [] 
    LETTER_POOL_02 = {}
    for key, value in LETTER_POOL.items():
        LETTER_POOL_02[key] = value
    
    
    while len(ten_letters) < 10:
        selection = random.choice(list(LETTER_POOL_02))
        if selection in LETTER_POOL:
            LETTER_POOL_02[selection] -= 1
            if LETTER_POOL_02[selection] < 1:
                LETTER_POOL_02.pop(selection)
            ten_letters.append(selection)
    return ten_letters



def uses_available_letters(word, letter_bank):
    """
    check if the word is an anagram of some or all of the given letters in the letter bank

    created a freq dict of letter_bank: letter_bank_dict
    created a freq dict of word: word_dict
    for letter in word_dict:
        if letter in letter_bank_dict:
            if word_dict[letter] < letter_bank_dict[letter]  #compare the freq of same letter
            return True

    input.upper()
    created a freq dict of letter_bank: letter_bank_dict
    for letter in word:
        if letter in letter_bank_dict:
            letter_bank_dict[letter] -= 1
            if letter_bank_dict[letter] < 1:
                return False
            else: 
                return True        
    """

    letter_bank = draw_letters()
    letter_bank_dict = {}
    for letter in letter_bank:
        if letter in letter_bank_dict:
            letter_bank_dict[letter] += 1
        else:
            letter_bank_dict[letter] = 1

    for letter in word:
        if letter in letter_bank_dict:
            letter_bank_dict[letter] -= 1
            if letter_bank_dict[letter] < 1:
                return False
            else:
                return True    



def score_word(word):
    """
    input: word
    output: total score of the word: sum of letters' point value + bonus of lenth value 8 (if lenth >= 7)
    score= 0
    for letter in word:
        for key, value in score_chart:
            if letter in value:
                score += key

    if lenth > 7 and lenth < 11:
        score += 8

    """

    

    
def get_highest_word_score(word_list):
    """
    input: word_list
    output: (winning word, score)
    tie-break rules: 10 letters > fewer letters  or  1st one if lenth is same
    """
    pass

