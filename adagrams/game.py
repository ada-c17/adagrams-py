def draw_letters():
    """
    import string package to import letters.
    import random to select random letters from a list
    import repeat to add repetative letters to our list
    import sample to select each letter only once
    """
    import string
    import random
    from itertools import repeat
    from random import sample
    """
    create a list of letters
    """
    letters = list(string.ascii_uppercase)
    """
    create a frequency list in order
    """
    frequency = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,8,2,1,6,4,6,4,2,2,1,2,1]
    """
    iterate over the letters list and add repeated items using the frequency-1
    """
    for i in range(len(letters)):
        letters.extend(repeat(letters[i],frequency[i]-1))
    
    """
    obtain a sample of ten letters
    """
    selection =  sample(letters,10)
    return selection


    # pass
draw_letters()
def uses_available_letters(word, letter_bank):
    """
    Turn all letters to uppercases if they are not already uppercase
    """
    if not word.isupper():
        word = word.upper()
    """
    make a copy of the letter_bank list
    remove every letter of the word from the bank
    count the number of letters that are in the bank
    """
    counter = 0
    bank = letter_bank.copy()
    for letter in word:
        if letter in bank:
            counter += 1
            bank.remove(letter)
    """
    return True when all of the letters of the word was in the bank
    """
    return counter == len(word)
    # pass
uses_available_letters("alex", ["A","B","C","D"])
def score_word(word):

    """
    return 0 if the word is empty
    """
    if not word:
        return 0
    
    word=word.upper()
    """
    add 7 scores if the lenght is between 7 and 10
    """
    score = 0
    if 7 <= len(word) <= 10:
        score += 8

    my_dic= { "A":1, "E":1, "I" :1, "O":1, "U" :1, "L" :1, "N" :1, "R":1, "S":1, "T" : 1,
    "D":2, "G":2,
    "B":3, "C":3, "M":3, "P":3,
    "F":4, "H":4, "V":4, "W":4, "Y":4,
    "K":5,
    "J":8, "X":8,
    "Q":10, "Z": 10}
    """
    loop over the word elements, find the element key in my_dic dictionary \ 
    and add the related score (related value) to the result
    """
    for element in word:
        if element in my_dic:
            score += my_dic[element]
    return score
    """
    Following is an alternative Approach
    """
    # if not word.isupper():
    #     word = word.upper()
    # score_one = {1:["A","E","I","O","U","L","N","R","S","T"],2:["D","G"],3:["B", "C", "M", "P"],4:["F", "H", "V", "W", "Y"],5: ["k"], 8:["J","X"], 10:["Q","Z"]}
    # total_score = 0
    # for letter in word:
    #     for score, letters in score_one.items(): 
    #         if letter in letters:
    #             total_score += score
    # if 7 <= len(word) <= 10:
    #     total_score += 8
    
    # return total_score



def get_highest_word_score(word_list):

    counter=0
    """
    loop over the word_list, calculate the score by calling score_word function
    compare the score with the one that is stored in counter and update the counter variable if 
    the new score is higher than the previous one
    elif another word with the same highest score was found apply 
    further criteria to select the result
    """
    for word in word_list:
        word_score = score_word(word)
        if word_score > counter:
            res = (word, word_score)
            counter = word_score
        elif word_score == counter and len(res[0]) != 10:
        
            if len(word) == 10 or len(word) < len(res[0]):
                res = (word, word_score)
            
    return res

    """
    Following is an alternative Approach
    """
    # def get_highest_word_score(word_list):
    # highest_word = ""
    # highest_score = 0
    # for word in word_list:
    #     score = score_word(word)
    #     if score > highest_score or \
    #         (score == highest_score and len(word) > len(highest_word) and len(word) == 10) or \
    #         score == highest_score and len(highest_word) != 10 and len(word) < len(highest_word):
    #         highest_word = word
    #         highest_score = score
    # return highest_word, highest_score
