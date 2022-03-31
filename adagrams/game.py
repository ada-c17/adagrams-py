#testing commit 
from copy import deepcopy
import random



def draw_letters():
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

    letter_key_list = list(LETTER_POOL.keys())
    random.shuffle(letter_key_list)
    
    letter_list = []
    for letter in letter_key_list:
        if LETTER_POOL[letter] > 0:
            if len(letter_list) < 10:
                letter_list.append(letter)
            
    return letter_list

#=====another example==========
# def draw_letters():
#     # Each time when we cal the function it will create new pool by appending keys v(value)timeseach in our list
#     # Invoking this function will not change the original pool of letters
#     #========creating new pool of letters==============
#     pool=[] 
#     for k,v in LETTER_POOL.items():
#         count=0
#         while count <v:
#             pool.append(k)
#             count+=1

#     #======creating hand of letters=================
#     #hand - random letters that the player has drawn [list of 10]
#     hand=[]
#     counter=0
#     while counter <10:# creating random index from 0 to 10
#         random_inex=random.randint(0, len(pool)-1)
#         hand.append(pool[random_inex])   #adding randomly picked letter to our hand (list of 10) 
#         pool.pop(random_inex)   #removing the same element from the pool 
#         counter+=1
#     return hand        
    
def uses_available_letters(word, letter_bank):
    pool = deepcopy(letter_bank)
    pool = [p.upper() for p in pool] # convert each element in a list to uppercase
    #print(pool)
    #print("============")
    for letter in word:
        if letter.upper() not in pool:
            return False
        else:
            pool.remove(letter.upper())
    return True   
 

#======another example============
# def uses_available_letters(word, letter_bank):
#     pass
#     letter_bank_dict = {}
#     for letter in letter_bank:
#         if letter not in letter_bank_dict:
#             letter_bank_dict[letter] = 1
#         elif letter in letter_bank_dict:
#             letter_bank_dict[letter] += 1
            
#     new_word = ""
#     for letter in word:
#         if letter.upper() in letter_bank_dict:
#             if letter_bank_dict[letter.upper()] > 0:
#                 letter_bank_dict[letter.upper()] -= 1
#                 new_word = new_word+letter
#             else:
#                 return False
                
#     if word == new_word:
#         return True
#     else:
#         return False


def score_word(word):
    
    list_1 = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    list_2 = ["D", "G"]
    list_3 = ["B", "C", "M", "P"]
    list_4 = ["F", "H", "V", "W", "Y"]
    list_5 = ["K"]
    list_6 = ["J", "X"]
    list_7 = ["Q", "Z"]
    
    total_points = 0
    
    for letter in word:
        if letter.upper() in list_1:
            total_points += 1
        elif letter.upper() in list_2:
            total_points += 2
        elif letter.upper() in list_3:
            total_points += 3
        elif letter.upper() in list_4:
            total_points += 4
        elif letter.upper() in list_5:
            total_points += 5
        elif letter.upper() in list_6:
            total_points += 8
        elif letter.upper() in list_7:
            total_points += 10
    
    if  len(word)>=7 and len(word)<=10:
        total_points+=8
 
    return total_points


def get_highest_word_score(word_list):
    dict_of_words={}
    for word in word_list:
        score =score_word(word)
        dict_of_words[word]=score   

    highest_score=0
    highest_score_words=[]

    for k,v in dict_of_words.items():
        if v>highest_score:
            highest_score=v
            highest_score_words.clear()
            highest_score_words.append(k)
        elif v==highest_score:
            highest_score_words.append(k)

    highest_score_word=highest_score_words[0]
    for e in highest_score_words:
         if len(e) >=10:
            highest_score_word=e
            break       
         elif len(e)<len(highest_score_word):
            highest_score_word=e
       
    result=tuple([highest_score_word,highest_score])    
    return result    



           

        




