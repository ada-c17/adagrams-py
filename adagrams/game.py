from copy import copy
from operator import indexOf
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

def draw_letters():
    OUR_POOL=copy.deepcopy(LETTER_POOL)
    array_of_letters = []
    while len(array_of_letters) < 10:
        letter = random.choice(list(OUR_POOL)).upper()
        if OUR_POOL[letter] != 0:
            array_of_letters.append(letter)
            OUR_POOL[letter] -= 1
    return array_of_letters
 

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
LETTER_SCORE = {
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
OUR_POOL = copy.deepcopy(LETTER_POOL)

def draw_letters():
    '''
    make an list to keep letters from the word if that letters is in the pool
    make deep copy of OUR_POOL of letters
    run while loop till the length is less than 10
        pick random letter from the pool
        if value of letter is 0 -> continue to next iteration
        if not, add letter to array_of_letters
        decrease value of letter (in pool dictionary) by 1
    return array_of_letters
    '''
    array_of_letters = []
    our_pool = copy.deepcopy(OUR_POOL)
    while len(array_of_letters) < 10:
        letter = random.choice(list(our_pool))
        if our_pool[letter] == 0:
            continue
        array_of_letters.append(letter)
        our_pool[letter] -= 1
            

    return array_of_letters
# print(draw_letters())
    

def uses_available_letters(word, letter_bank):
    '''
    if letter from the word is not in the bank return False
    if letter from the word is in the bank, replace that letter
    with True in the bank

    Count True in the letter bank
    if count of True in the bank is equal to length of word return True
    otherwise return False
    '''
    our_bank = copy.deepcopy(letter_bank)
    word1 = copy.deepcopy(word).upper()

    for i in range (len(word1)):
        if word1[i] in our_bank:
            index_of_letter = our_bank.index(word1[i]) #take extra time to get the index
            our_bank[index_of_letter] = True
    
    if our_bank.count(True) == len(word1):
        return True
    else:
        return False
    

uses_available_letters("apple", ['N', 'F', 'M', 'L', 'I', 'D', 'P', 'I', 'F', 'D']) 


 
def score_word(word):
    score_chart={"A":1, "E":1, "I":1, "O":1, "U":1, "L":1, "N":1, "R":1, "S":1, "T":1, "D":2,"G":2, "B":3,"C":3,"M":3,"P":3,"F":4,"H":4,"V":4, "W":4, "Y":4,"K": 5, "J":8,"X":8,"Q":10,"Z":10}
   
    #checkevery element in word
    #if element in chart add its value to a list then give me the sum of the list/if words length is 7-8-9-10 add 8 to the result
    
    result=[]
    copied_word=copy.deepcopy(word).upper()
    
    for i in copied_word:
        # ?????????
        if i in score_chart:
            result.append(score_chart[i])
    if len(copied_word)==8 or len(copied_word)==9 or len(copied_word)==10 or len(copied_word)==7:
            result.append(8)
    score =sum(result)
    return score

# def get_highest_word_score(word_list):
#     list1=[]
#     for item in word_list:
#         score=score_word(item)
#         list1.append(score)
#     print(list1)
#     print (item,max(list1))
#     return (item,max(list1))

        
# get_highest_word_score(["XXX", "XXXX", "XX", "X"])    

def get_highest_word_score(word_list):
#     ‘’'
#     # set highest score to the score of the first word
#     # use loop to get the highest score: if current score is greater or equal
#       to highest score, set highest score to current score
#     # use list comprehension and get the list of words with highest score
#     # from the list of highest score words we need return word with length of 10
#     if exist, or word with minimum length if there is no 10 length word, so:
#         get list of len 10 words (or empty if no such word) using list comprehention
#         get word with min length using min function
#     # if list of words with length of ten exist: return it’s first element
#         otherwise return word of minimum length
# What?????
    highest_score = score_word(word_list[0])
    #highest is the first of the list
    for word in word_list:
        if score_word(word) >= highest_score:
            #highest are the ones bigger or same as first of the list
            highest_score = score_word(word)
    #what is this doing???????
    list_of_highest_score_words = [word for word in word_list \
        if score_word(word) == highest_score]
        #we have list of the highest words
    ten_len_word = [word for word in list_of_highest_score_words if len(word) == 10]
   #what????????
    min_len_word = min((word for word in list_of_highest_score_words if word), key=len)
    #what
    return [ten_len_word[0], highest_score] if ten_len_word else [min_len_word, highest_score]







    '''
    if empty word return 0
    if length of word greater than 6, set initial score to 8, otherwise to 0
    using loop add each letter's value to score
    '''
    word1 = copy.deepcopy(word).upper()
    # if not word:
    #     return 0
    score = 8 if len(word1) > 6 else 0
    for letter in word1:
        score += LETTER_SCORE[letter]
    
    return score
print(score_word("CUCUmber"))

def get_highest_word_score(word_list):
    '''
    # set highest score to the score of the first word
    # use loop to get the highest score: if current score is greater or equal 
      to highest score, set highest score to current score
    # use list comprehension and get the list of words with highest score
    # from the list of highest score words we need return word with length of 10
    if exist, or word with minimum length if there is no 10 length word, so:
        get list of len 10 words (or empty if no such word) using list comprehention
        get word with min length using min function
    # if list of words with length of ten exist: return it's first element
        otherwise return word of minimum length
    
    '''
    highest_score = score_word(word_list[0])
    for word in word_list:
        if score_word(word) >= highest_score:
            highest_score = score_word(word)
    
    list_of_highest_score_words = [word for word in word_list \
        if score_word(word) == highest_score]

    ten_len_word = [word for word in list_of_highest_score_words if len(word) == 10]
    min_len_word = min((word for word in list_of_highest_score_words if word), key=len)
    
    return [ten_len_word[0], highest_score] if ten_len_word else [min_len_word, highest_score]
    

    print(list_of_highest_score_words)

get_highest_word_score(["AAAAAAAAAA", "EEEEEEEEEE"])
