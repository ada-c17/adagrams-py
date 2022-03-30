
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

scores_chart = {
    "A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2, 
    "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3, 
    "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1, 
    "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4, 
    "X": 8, "Z": 10
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

    # letter_bank = draw_letters()
    letter_bank_dict = {}
    word = word.upper()
    for letter in letter_bank:
        if letter in letter_bank_dict:
            letter_bank_dict[letter] += 1
        else:
            letter_bank_dict[letter] = 1
 

    for letter in word:
        if letter in letter_bank_dict:
            letter_bank_dict[letter] -= 1
            if letter_bank_dict[letter] < 0:
                return False
        
        else:
            return False
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



scores_chart = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2, 
         "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3, 
         "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1, 
         "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4, 
         "X": 8, "Z": 10}
    """
    word = word.upper()
    score = 0
    for letter in word:
        score += scores_chart[letter]
    if len(word) >= 7 and len(word)< 11:
        # if len(word) == 7 or len(word) == 8 or len(word) == 9 or len(word) == 10:
        # if len(word) in [7, 8, 9, 10]:
        score +=  8

    return score 
    

    
def get_highest_word_score(word_list):
    """
    input: word_list
    output: (winning word, score)
    tie-break rules: 10 letters > fewer letters  or  1st one if lenth is same
    """

    winning_words = []
    score_dict = {}
    winner = ""
    for word in word_list:
        score_dict[word] = score_word(word)
    
    max_score = max(score_dict.values())
    for key, value in score_dict.items():
        if value == max_score:
            winning_words.append(key) 
    # to get words with highest score include case with more than 1 highest score
    
    if len(winning_words) == 1:
        winner = winning_words[0]
    
    else: 

        for i in range(len(winning_words)):
            if len(winning_words[i]) == 10:
                winner = winning_words[i]
                break
            #when return the first word that has a lenth of 10 no matter how many lenth 10 words in the list

            else:
                min_lenth = len(winning_words[0])
                for i in range(len(winning_words)):
                    if len(winning_words[i]) < min_lenth:
                        min_lenth = len(winning_words[i]) 
                        # to deside the min leth in the winning_words list
                        
                if len(winning_words[i]) == min_lenth:
                    winner = winning_words[i]
                    break
            # return the first min lenth word no matter how many of them in the list
    winner_list = [winner, score_word(winner)]
    return tuple(winner_list)    

