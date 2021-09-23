import copy
import random

class Hand:
    def __init__(self, letter_pool):
        self.letter_pool = letter_pool
        self.letter_bank = []
        self.draw_letters()

    def draw_letters(self):
        letter_pool_copy = copy.deepcopy(self.letter_pool)

        while len(self.letter_bank) < 10:
            letter = random.choice(list(letter_pool_copy.keys()))
            if letter_pool_copy[letter] > 0:
                self.letter_bank.append(letter)
                letter_pool_copy[letter] -= 1

    def uses_available_letters(self, word):
        letter_bank_copy = copy.deepcopy(self.letter_bank)

        for letter in word:
            letter = letter.upper()
            if letter in letter_bank_copy:
                letter_bank_copy.remove(letter)
            else:
                return False
        
        return True
