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







