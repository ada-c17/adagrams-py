score_chart = {
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
    'P': 2, 
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

word = "structure"
cap_word = word.upper()

def score_word(word):   
    total_score = 0

    if word == " ":
        return total_score

    if len(word) >= 7 and len(word) <= 10:
        total_score += 8

    for letter in cap_word:
        total_score += score_chart[letter]
    
    print(total_score)
    

score_word(word)
    

# import collections


# letters = ["D", "O", "G", "X", "X", "X", "X", "X", "X", "X"]
# word = "DOG"

# def uses_available_letters(word, letter_bank):
    
#     word_freq = collections.Counter(word)
#     letters_freq = collections.Counter(letters)
#     for letter in word_freq:
#         if word_freq[letter] > letters_freq[letter]:
#             return False
#         else:
#             return True
# results = uses_available_letters(word, letters)
# print(results)













# import random

# def generate_random_letter(x,y):

#     return  chr(random.randint(ord(x),ord(y)))

# letters= []
# pool_of_letters = {
#     'A' : 9,
#     'B' : 2,
#     'C' : 2,
#     'D' : 4,
#     'E' : 12,
#     'F' : 2,
#     'G' : 3,
#     'H' : 2,
#     'I' : 9,
#     'J' : 1,
#     'K' : 1,
#     'L' : 4,
#     'M' : 2,
#     'N' : 6,
#     'O' : 8,
#     'P' : 2,
#     'Q' : 1,
#     'R' : 6,
#     'S' : 4,
#     'T' : 6,
#     'U' : 4,
#     'V' : 2,
#     'W' : 2,
#     'X' : 1,
#     'Y' : 2,
#     'Z' : 1,
# }

# # print(pool_of_letters)

# def draw_letter():
#     count = 1
#     while count <= 10:
#         random_letter = generate_random_letter("A", "Z")
#         # temp_key = random_letter
#         # generates random letter from a-z
#          # compares letter against distribution dictionary
#         # if pool_of_letters[temp_key] == 0:
#         #     temp_key = " "
#         # else:
#         letters.append(random_letter)
#         count += 1
#         pool_of_letters[random_letter] -= 1
#         print(letters)

        
#         # for letter in  letters:
#         #     if letter in pool_of_letters:
#         #         pool_of_letters[letter] += 1]
#         # updates letter count in dictionary

       

#         # adds letter to letters []
#         # problem- no vowels generated
#         # letters.append(random_letter)
#         # count += 1
    
# draw_letter()





