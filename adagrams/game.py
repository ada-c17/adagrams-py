def draw_letters():
    import string
    import random
    from itertools import repeat
    from random import sample
    letters = list(string.ascii_uppercase)
    
    frequency = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]
    
    for i in range(len(letters)):
        letters.extend(repeat(letters[i],frequency[i]-1))
    print (letters)
    selection =  sample(letters,10)
    # for i in range(10):
    #     selection.append(random.sample(letters))
    # print (selection)
    return selection

    # pass
draw_letters()
def uses_available_letters(word, letter_bank):
    if not word.isupper():
        word = word.upper()
    counter = 0
    bank = letter_bank.copy()
    known_letter = []
    for letter in word:
        if letter in bank:
            counter += 1
            bank.remove(letter)
    
    return counter == len(word)
    # pass
uses_available_letters("alex", ["A","B","C","D"])
def score_word(word):
    res=0
    if not word:
        return res
    word=word.upper()
    if 7<=len(word)<=10:
        res+=8
    my_dic= { "A":1, "E":1, "I" :1, "O":1, "U" :1, "L" :1, "N" :1, "R":1, "S":1, "T" : 1,
    "D":2, "G":2,
    "B":3, "C":3, "M":3, "P":3,
    "F":4, "H":4, "V":4, "W":4, "Y":4,
    "K":5,
    "J":8, "X":8,
    "Q":10, "Z": 10}
    for ele in word:
        if ele in my_dic:
            res+=my_dic[ele]
    return res
def get_highest_word_score(word_list):
    counter=0
    
    for word in word_list:
        word_score=score_word(word)
        if word_score>counter:
            res=(word, word_score)
            counter=word_score
        elif word_score == counter and len(res[0]) != 10:
        
            if len(word) == 10 or len(word) < len(res[0]):
                res = (word, word_score)
            
    return res
