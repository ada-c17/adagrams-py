import random

'''
Your first task is to build a hand of 10 letters for the user. 
To do so, implement the function `draw_letters` in `game.py`. 
This method should have the following properties:

- No parameters
- Returns an array of ten strings
  - Each string should contain exactly one letter
  - These represent the hand of letters that the player has drawn
- The letters should be randomly drawn from a pool of letters
  - This letter pool should reflect the distribution of letters as described in the table below
  - There are only 2 available `C` letters, so `draw_letters` cannot ever return more than 2 `C`s
  - Since there are 12 `E`s but only 1 `Z`, it should be 12 times as likely for the 
  user to draw an `E` as a `Z`
- Invoking this function should **not** change the pool of letters
  - Imagine that the user returns their hand to the pool before drawing new letters

| Letter : Qty. | Letter : Qty. |
|:------:|:-----:|
| A : 9  | N : 6 |
| B : 2  | O : 8 |
| C : 2  | P : 2 |
| D : 4  | Q : 1 |
| E : 12 | R : 6 |
| F : 2  | S : 4 |
| G : 3  | T : 6 |
| H : 2  | U : 4 |
| I : 9  | V : 2 |
| J : 1  | W : 2 |
| K : 1  | X : 1 |
| L : 4  | Y : 2 |
| M : 2  | Z : 1 |
'''

LETTER_QUANTITY_DICT = {'A' : 9, 'N' : 6 ,
'B' : 2, 'O' : 8, 
'C' : 2, 'P' : 2, 
'D' : 4, 'Q' : 1, 
'E' : 12,'R' : 6,
'F' : 2, 'S' : 4, 
'G' : 3, 'T' : 6,
'H' : 2, 'U' : 4,
'I' : 9, 'V' : 2, 
'J' : 1, 'W' : 2,
'K' : 1, 'X' : 1, 
'L' : 4, 'Y' : 2,
'M' : 2, 'Z' : 1}
# Set Distribution of Letters to Global Variables (Dictionary)
# Letter as key, Quantity as value

def draw_letters():
    letter_list = []

    for letter, quantity in LETTER_QUANTITY_DICT.items():
      counter = 0
      while counter < quantity:
          letter_list.append(letter)
          counter += 1
    
    letter_bank = random.sample(letter_list, 10)

    return letter_bank


'''
Next, you need a way to check if an input word (a word a player submits) 
only uses characters that are contained within a collection (or hand) of drawn letters. 
Essentially, you need a way to check if the word is an anagram of some or all of the given 
letters in the hand.

To do so, implement the function called `uses_available_letters` in `game.py`. 
This function should have the following properties:

- Has two parameters:
   - `word`, the first parameter, describes some input word, and is a string
   - `letter_bank`, the second parameter, describes an array of drawn letters in a hand. 
   You can expect this to be an array of ten strings, with each string representing a letter
- Returns either `True` or `False`
- Returns `True` if every letter in the `input` word is available (in the right quantities) 
in the `letter_bank`
- Returns `False` if not; if there is a letter in `input` that is not present in the 
`letter_bank` or has too much of compared to the `letter_bank`
'''

def uses_available_letters(word, letter_bank):
#    return true or false if the word has the correct letter quantities in the word bank
#  Check if word is valid 
# Loop through word to append to list. List for element in the word
# - Helper function if letter is in list- 
# - Return False if not in list
# If letter.count in word <= letter count in list Return True,
#  If not correct quantity return False

    
    pass

""" ### Wave 3: score_word

Now you need a function returns the score of a given word as defined by the Adagrams game.

Implement the function `score_word` in `game.py`. This method should have the following properties:

- Has one parameter: `word`, which is a string of characters
- Returns an integer representing the number of points
- Each letter within `word` has a point value. The number of points of each 
letter is summed up to represent the total score of `word`
- Each letter's point value is described in the table below
- If the length of the word is 7, 8, 9, or 10, then the 
word gets an additional 8 points

#### Score chart

|Letter                        | Value|
|:----------------------------:|:----:|
|A, E, I, O, U, L, N, R, S, T  |   1  |
|D, G                          |   2  |
|B, C, M, P                    |   3  |
|F, H, V, W, Y                 |   4  |
|K                             |   5  |
|J, X                          |   8  |
|Q, Z                          |   10 | """

def score_word(word):
    # Output: Total points from the word made from the letter_bank
    # check if the word is valid. if word is not valid, return none.
    # loop through the word and put each letter in a list
    # make variable called total points
    # make a dictionary that has the score chart
    # - with score value as 'key' and the letters are in a list as values
    # make a for loop with scoring conditions...
    # example: if the "a" is in dictionary's value, add 1 point to the points
    # check length of word with conditionals of extra points
    total_score = 0
    letter_list = []

    score_chart = {
      1:["A","B","I","O","U","L","N","R","S","T"],
      2:["D","G"],
      3:["B","C","M","P"],
      4:["F","H","V","W","Y"],
      5:["K"],
      8:["J","X"],
      10:["Q","Z"]
    }
    extra_score_chart = [7, 8, 9, 10]

    if word == "":
        return total_score

    for letter in word:
        letter_list.append(letter)

    for letter in letter_list:
        if letter in score_chart.values():
            pass
    
    if len(word) in extra_score_chart:
        total_score += 8
    
    return letter_list

print(score_word("dog"))



"""### Wave 4: get_highest_word_score

After several hands have been drawn, words have been submitted, checked, scored, and played, you need a way to find the highest scoring word. This function looks at the list of `word_list` and calculates which of these words has the highest score, applies any tie-breaking logic, and returns the winning word in a special data structure.

Implement a function called `get_highest_word_score` in `game.py`. This method should have the following properties:

- Has one parameter: `word_list`, which is a list of strings
- Returns a tuple that represents the data of a winning word and it's score.  The tuple must contain the following elements:
  - index 0 ([0]): a string of a word
  - index 1 ([1]): the score of that word
- In the case of tie in scores, use these tie-breaking rules:
    - prefer the word with the fewest letters...
    - ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
    - If the there are multiple words that are the same score and the same length, pick the first one in the supplied list"""

def get_highest_word_score(word_list):
    pass