import random 

class Hand:
    def __init__(self, letter_pool):
        self.letter_bank = self.draw_letters(letter_pool)
    
    def draw_letters(self, letter_pool):
        letters = {'A': 9, 'B': 2, 'O': 8, 'C': 2, 'P': 2, 
                        'D': 4, 'Q': 1, 'E': 12, 'R': 6, 'F': 2, 
                        'S': 4, 'G': 3, 'T': 6, 'H': 2, 'U': 4, 
                        'I': 9, 'V': 2, 'J': 1, 'W': 2, 'K': 1, 
                        'X': 1, 'L': 4, 'Y': 2, 'M': 2, 'Z': 1}
        hand = []

        while len(hand) < 10:
            letter = random.choice(list(letters))
            if letters[letter] > 0:
                hand.append(letter)
                letters[letter] -= 1
        return hand


    def uses_available_letters(self, word):
        is_anagram = True
        letters = list(self.letter_bank)
        
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                is_anagram = False

        return is_anagram