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

def draw_letters():
    import string
    import random
    import copy

    user_hand = []
    # deepcopy makes a copy that has its own reference in memory so that we don't
    # overwrite the original list
    temp_dict = copy.deepcopy(LETTER_POOL)

    while len(user_hand) < 10:
        # random.choice selects a random letter from the string we give it and then
        # string.ascii_uppercase gives us a string of all 26 letters in upper case form
        letter = random.choice(string.ascii_uppercase)
        letter_count = temp_dict[letter]
        if letter_count == 0:
            continue
        else:
            temp_dict[letter] -= 1
            user_hand.append(letter)

    return user_hand


def uses_available_letters(word, letter_bank):
    # .upper returns a string where all characters are uppercase
    word = word.upper()
    for letter in word:
        # .count returns the number of times the letter is found within that word
        letter_count = word.count(letter)
        bank_count = letter_bank.count(letter)
        if letter in letter_bank:
            if letter_count <= bank_count:
                continue 
            else:
                return False
        else: 
            return False
    return True

def score_word(word):
    letter_vals = {
        "A": 1, 
        "B": 3, 
        "C": 3, 
        "D": 2, 
        "E": 1, 
        "F": 4, 
        "G": 2, 
        "H": 4, 
        "I": 1, 
        "J": 8, 
        "K": 5, 
        "L": 1, 
        "M": 3, 
        "N": 1, 
        "O": 1, 
        "P": 3, 
        "Q": 10, 
        "R": 1, 
        "S": 1, 
        "T": 1, 
        "U": 1, 
        "V": 4, 
        "W": 4, 
        "X": 8, 
        "Y": 4, 
        "Z": 10 }

    final_score = 0
    letter_count = 0
    length = len(word)

    word = word.upper()

    for char in word:
        letter_count = letter_vals[char]
        final_score += letter_count

    if 7 <= length <= 10:
        final_score += 8   



    return final_score

def tie_breaker(max_score):
    tie = []
    counter = 1000
    length = len(max_score)

    for i in range(length):
        if length == 10:
            tie.append(max_score[i])
            return tie
        else: 
            if counter == length:
                continue
            else:
                counter = length
                tie.append(max_score[i])

def tie_breaker(max_score):
    tie = ["", 0]
    smallest_word_len = 1000
    

    for i in range(len(max_score)):
        word = max_score[i][0]
        score = max_score[i][1]
        length = len(word)

        if length == 10:
            # .clear() method removes all elements  from a list
            tie.clear()
            tie.append(word)
            tie.append(score)
            break
        elif length < smallest_word_len:
            smallest_word_len = length
            tie.clear()
            tie.append(word)
            tie.append(score)
        else:
            continue           

    return tie

def get_highest_word_score(word_list):
    word_score = 0
    winner_list = []
    max_score = [["", 0]]
    score_tuple = tuple() 

    for word in word_list:
        i = 0
        word_score = score_word(word)
        if word_score > max_score[i][1]:
            max_score.clear()
            max_score.append([word, word_score])
        elif word_score == max_score[i][1]:
            max_score.append([word, word_score])
        else:
            continue
        i += 1
    
    if len(max_score) > 1:
        tie = tie_breaker(max_score)
        score_tuple = tuple(tie)
    else:
        winner_list.append(max_score[0][0])
        winner_list.append(max_score[0][1])
        score_tuple = tuple(winner_list)

    return score_tuple