
import random
import copy
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
#Wave 1 (Bahareh)
def draw_letters():
    OUR_POOL=copy.deepcopy(LETTER_POOL)
    array_of_letters = []
    while len(array_of_letters) < 10:
        letter = random.choice(list(OUR_POOL)).upper()
        if OUR_POOL[letter] != 0:
            array_of_letters.append(letter)
            OUR_POOL[letter] -= 1
    return array_of_letters
 
#Wave 2 (Bahareh)
def uses_available_letters(word,letter_bank):
    copied_word=copy.deepcopy(word).upper()
    copied_bank = copy.deepcopy(letter_bank)
    empty_list=[]
    for i in copied_word:
       if i in copied_bank:
            empty_list.append(i)
            copied_bank.remove(i)
            
    if len(empty_list)==len(word):
        return True
    else: 
        return False

#Waive 3 (Bahareh)
def score_word(word):
    score_chart={"A":1, "E":1, "I":1, "O":1, "U":1, "L":1, "N":1, "R":1, "S":1, "T":1, "D":2,"G":2, "B":3,"C":3,"M":3,"P":3,"F":4,"H":4,"V":4, "W":4, "Y":4,"K": 5, "J":8,"X":8,"Q":10,"Z":10}
    result=[]
    copied_word=copy.deepcopy(word).upper()
    
    for i in copied_word:
        if i in score_chart:
            result.append(score_chart[i])
    if len(copied_word)==8 or len(copied_word)==9 or len(copied_word)==10 or len(copied_word)==7:
            result.append(8)
    score =sum(result)
    return score



    
   
