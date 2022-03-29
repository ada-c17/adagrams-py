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

def uses_available_letters(word, letter_bank):
    if not word.isupper():
        word = word.upper()
    counter = 0
    bank = letter_bank.copy()
    for letter in word:
        if letter in bank:
            counter += 1
            bank.remove(letter)

    return counter == len(word)
    # pass

def score_word(word):
    if not word.isupper():
        word = word.upper()
    score_one = {1:["A","E","I","O","U","L","N","R","S","T"],2:["D","G"],3:["B", "C", "M", "P"],4:["F", "H", "V", "W", "Y"],5: ["k"], 8:["J","X"], 10:["Q","Z"]}
    total_score = 0
    for letter in word:
        for score, letters in score_one.items(): 
            if letter in letters:
                total_score += score
    if 7 <= len(word) <= 10:
        total_score += 8
    print (total_score)
    return total_score

def get_highest_word_score(word_list):
    highest_word = ""
    highest_score = 0
    for word in word_list:
        score = score_word(word)
        if score > highest_score or \
            (score == highest_score and len(word) > len(highest_word) and len(word) == 10) or \
            score == highest_score and len(highest_word) != 10 and len(word) < len(highest_word):
            highest_word = word
            highest_score = score
    return highest_word, highest_score

    # dic = {}
    # for wordle in word_list:
    #     dic[wordle] = score_word(wordle)
    # a = max(dic.values())
    # print (dic)
    
    # max_keys = []

    # for key,value in dic.items():
    #     if value == a and value:
    #         max_keys.append(key)
    # y = sorted(max_keys, key=len)
    # for string in max_keys:
    #     list2 = list(map(lambda x: len(x)  , y))
    #     if len(string) == 10:
    #         output = (string,a)
    #     else:
    #         output = (y[0],a)

    # print(output)
    # return output
    # dic = {}
    # for wordle in word_list:
    #     dic[wordle] = score_word(wordle)
    # print (dic)

    # output = (max(dic, key=dic.get),max(dic.values()))
    # if len(output) > 2:

    # print (output)
    # return output
    # return max(list(map(lambda word: score_word(word)  , word_list)))

    # pass