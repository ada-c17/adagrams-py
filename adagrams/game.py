import random
import copy

def draw_letters():
    
    letter_frequency = {
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
    
    letter_pool = []
    letter_bank = []
    #generate elements for letter_pool list in correct frequency
    for letter, frequency in letter_frequency.items(): 
        for _ in range(frequency):
            letter_pool.append(letter)
    #selecting the letters for gameplay from letter_pool list
    while len(letter_bank) < 10:
        letter = random.choice(letter_pool)
        letter_pool.remove(letter)
        letter_bank.append(letter)

    return letter_bank


def uses_available_letters(word, letter_bank):

    letter_bank_copy = copy.deepcopy(letter_bank)
    uppercase_word = word.upper()
    #checking that each letter used in word is available in letter_bank and in sufficient quantity
    for letter in uppercase_word: 
        if letter not in letter_bank_copy:
            return False
        else: 
            letter_bank_copy.remove(letter)

    return True


def score_word(word):
    
    letter_points = {
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

    total_score = 0
    uppercase_word = word.upper()
    #iterating over each letter to get its value, totalling the value in total_score
    for letter in uppercase_word: 
        total_score += letter_points[letter]
    #adding 8 extra points if length of word is equal or more than 7
    if len(word) >= 7: 
        total_score += 8
    
    return total_score


def get_highest_word_score(word_list):
    
    best_words = []
    highest_score = 0
    #makes word_tuple and checks for the highest score. The highest scoring tuple(s) is appended to best_words list.
    for word in word_list:
        word_tuple = (word, score_word(word))
        if word_tuple[1] > highest_score:
            best_words = [word_tuple]
            highest_score = word_tuple[1]
        elif word_tuple[1] == highest_score:
            best_words.append(word_tuple)
    #if there is a tie for highest score, find winning word from best_words list
    if len(best_words) > 1:
        shortest_length_of_word = 10
        index_of_shortest_word = 0

        for index in range(len(best_words)): #iterates over the list
            if len(best_words[index][0]) == 10: #look at "word" part of tuple: ("word", score)
                return best_words[index] #return whole tuple
            elif len(best_words[index][0]) < shortest_length_of_word: #look at "word" part of tuple
                shortest_length_of_word = len(best_words[index][0])
                index_of_shortest_word = index
        return best_words[index_of_shortest_word]

    return best_words[0] #in a list of len 1 return tuple


    

