import random

def generate_random_letter(x,y):

    return  chr(random.randint(ord(x),ord(y)))

letters= []
pool_of_letters = {
    'A' : 9,
    'B' : 2,
    'C' : 2,
    'D' : 4,
    'E' : 12,
    'F' : 2,
    'G' : 3,
    'H' : 2,
    'I' : 9,
    'J' : 1,
    'K' : 1,
    'L' : 4,
    'M' : 2,
    'N' : 6,
    'O' : 8,
    'P' : 2,
    'Q' : 1,
    'R' : 6,
    'S' : 4,
    'T' : 6,
    'U' : 4,
    'V' : 2,
    'W' : 2,
    'X' : 1,
    'Y' : 2,
    'Z' : 1,
}

# print(pool_of_letters)

def draw_letter():
    count = 1
    while count <= 10:
        random_letter = generate_random_letter("A", "Z")
        # generates random letter from a-z
         # compares letter against distribution dictionary
        if pool_of_letters[random_letter] == 0:
            random_letter = " "
        else:
            letters.append(random_letter)
            count += 1
            pool_of_letters[random_letter] -= 1
       

        
        # for letter in  letters:
        #     if letter in pool_of_letters:
        #         pool_of_letters[letter] += 1]
        # updates letter count in dictionary

       

        # adds letter to letters []
        # problem- no vowels generated
        # letters.append(random_letter)
        # count += 1
    print(letters)
    print(pool_of_letters)
draw_letter()





