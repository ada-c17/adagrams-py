import random 

LETTER_POOL = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 
               'X': 1, 'Y': 2, 'Z': 1}

def draw_letters():
    letter_list = []

    # Put every available letter in a list. If X is available N times, there will be N X's in the list
    for key in LETTER_POOL:
        letter_list += key * LETTER_POOL[key]
    
    # shuffle the list
    random.shuffle(letter_list)

    # pick first 10 letters from the list
    output = letter_list[:10]
    
    return output
        
def uses_available_letters(word, letter_bank):
    # convert word to uppercase for case insensitive operations
    word_upper = word.upper()

    # compare count of each letter in word with count of that letter in letter_bank
    for letter in word_upper:
        # If a letter appears more times in word than in letter_bank than return False
        if word_upper.count(letter) > letter_bank.count(letter):
            return False
    return True

    
SCORE_CHART = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 
               'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}  

def score_word(word):
    score = 0

    # Calculate score
    for letter in word.upper():
        if letter in SCORE_CHART:
            score += SCORE_CHART[letter]
    
    # Add additional points if length is 7, 8, 9 or 10
    if 7 <= len(word) <= 10:
        score += 8

    return score
    

def get_highest_word_score(word_list):
    
    best = ("", 0)
    for i in range(len(word_list)):
        score = score_word(word_list[i]) #current word score 

        # Local flag variable, True indicate that the best needs to be updated
        update = False
        
        if score > best[1]:
            # Greater score for current word - need to update best
            update = True
        
        # Might need to update best if scores are equal and lengths different
        elif score == best[1] and len(word_list[i]) != len(best[0]):
            # If current word has length 10 need to update best
            if  len(word_list[i]) == 10:
                update = True
            
            # Update if best word doesn't have length 10 and length of current word is less than length of best word
            if len(best[0]) != 10 and len(word_list[i]) < len(best[0]):
                update = True

        # Update best if necessary
        if update:
            best = (word_list[i], score)

    return best
    

