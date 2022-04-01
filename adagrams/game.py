import random
myLetterPool = [
  {'A':9},
  {'B':2},
  {'C':2},
  {'D':4},
  {'E':12},
  {'F':2},
  {'G':3},
  {'H':2},
  {'I':9},
  {'J':1},
  {'K':1},
  {'L':4},
  {'M':2},
  {'N':6},
  {'O':8},
  {'P':2},
  {'Q':1},
  {'R':6},
  {'S':4},
  {'T':6},
  {'U':4},
  {'V':2},
  {'W':2},
  {'X':1},
  {'Y':2},
  {'Z':1}
]
def draw_letters():
    myLetters = []
    listOfLetters =[]
    
    for letter in myLetterPool:
        for key,value in letter.items():
            for i in range(value):
                listOfLetters.append(key)
    
    while len(myLetters) < 10:
        letterPick = random.randint(1,len(listOfLetters))
        myLetters.append(listOfLetters.pop(letterPick))
    return myLetters

def uses_available_letters(word, letter_bank):
    aCopy = listCopy(letter_bank)
    for letter in word:
        if letter.upper() in aCopy:
            aCopy.remove(letter.upper())
        else:
            return False
    return True
    pass

def listCopy(aList):
    listCopy = []
    for elem in aList:
        listCopy.append(elem)
    return listCopy

scoreChartDict = {
  1:["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
  2:["D", "G"],
  3:["B", "C", "M", "P"],
  4:["F", "H", "V", "W", "Y"],
  5:["K"],
  8:["J", "X"],
  10:["Q", "Z"]
}
def score_word(word):
    points = 0
    for letter in word:
        for key,value in scoreChartDict.items():
            if letter.upper() in value:
                points += key
    if len(word) >= 7 or len(word) >= 8 or len(word) >= 9 or len(word) >= 10:
        points += 8
    return points
    pass

def get_highest_word_score(word_list):
    highestScore = 0
    winningWord = ""
  
    for word in word_list:
        if score_word(word) > highestScore:
            highestScore = score_word(word)
            winningWord = word
    
        elif score_word(word) == highestScore:
            if len(word) == 10 and len(winningWord) != 10:
                winningWord = word
            if len(word) < len(winningWord) and len(winningWord) == 10:
                winningWord != word
            elif len(word) < len(winningWord):
                winningWord = word
        
    return (winningWord, highestScore)
    pass