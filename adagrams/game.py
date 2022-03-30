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
# -----test_wave_01-----------
def draw_letters():
    letter_list=[]
    #get all letters and repeats from the pool into a list
    # ex-if letter 'A' has a value of 2: should have ['A','A']
    for letter in LETTER_POOL:
        repeat_num=LETTER_POOL[letter]    
        letter_list.extend(letter*repeat_num)
    print(letter_list)
    
    new_letter_list=[]
    count_dict={}

<<<<<<< HEAD
    num_letters=0
    while num_letters <10:
        letter=random.choice(letter_list)
        if letter in count_dict:
            if count_dict[letter] < LETTER_POOL[letter]:
                count_dict[letter]+=1
                new_letter_list.append(letter)
                num_letters +=1
        else:
            count_dict[letter]=1
            new_letter_list.append(letter)
            num_letters +=1
    return new_letter_list

#-------test_wave_02---------------
def uses_available_letters(word, letter_bank):
    word = word.upper()
    
    for letter in word:
        keep_checking = True
        if letter in letter_bank:
            letter_count=word.count(letter)
            letter_list_count=letter_bank.count(letter)
            if letter_count <= letter_list_count:
                keep_checking    
            else:
                keep_checking = False
                break
        else:
            return False
    return keep_checking
#-----test_wave_03-----------
score_dict={
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
def score_word(word):
    score_point=0
    word=word.upper()
    for letter in word:
        score_point += score_dict[letter]
    if len(word) >=7:
        score_point+=8
    return score_point
#------test_wave04-------
def get_highest_word_score(word_list):
    
    # word_score_list=[]
    
    # for word in word_list:
    #     score=score_word(word)
    #     word_score_list.append({'word':word,'score':score})

    new_word_list = []
    new_score_list = []
    for word in word_list:
        for key in score_dict:
            if word == key:
                new_word_list.append(word)
                new_score_list.append(score_dict[key])

    highest_score = 0
    
    list_highest_score_word = []
    for i in range(len(new_word_list)):
        if new_score_list[i] > highest_score:
            highest_score = new_score_list[i]
            list_highest_score_word.append(new_word_list[i])

    # shortest_length=len(list_highest_score_word[0])
    # print(shortest_length)
    # final_sorted_list =[]

    # for word in list_highest_score_word:
    #     if len(word) < shortest_length:
    #         shortest_length = word
    #         final_sorted_list.append(word)

=======

def uses_available_letters(word, letter_bank):
    letters_valid = True
    letter_bank_copy = []
    for letter in letter_bank:
        letter_bank_copy.append(letter.upper())
    for letter in word:
        letter = letter.upper()
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            letters_valid = False
    return letters_valid


def score_word(word):

    points_dict = {}
    for letter in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]:
        points_dict[letter] = 1
    for letter in ["D", "G"]:
        points_dict[letter] = 2
    for letter in ["B", "C", "M", "P"]:
        points_dict[letter] = 3
    for letter in ["F", "H", "V", "W", "Y"]:
        points_dict[letter] = 4
    for letter in ["K"]:
        points_dict[letter] = 5
    for letter in ["J", "X"]:
        points_dict[letter] = 8
    for letter in ["Q", "Z"]:
        points_dict[letter] = 10

    score = 0

    for char in word.upper():
        if char not in points_dict:
            continue
        else:
            score += points_dict[char]
    if len(word) in range(7, 11):
        score += 8

    return score


def get_highest_word_score(word_list):
    pass
>>>>>>> 233ff992afa912cf5c18cea14d0161609a9068ae
