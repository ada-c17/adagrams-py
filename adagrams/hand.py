import copy

class Hand:
    def __init__(self, letter_bank):
        self.letter_banks = letter_bank

    def uses_available_letters(self, word):
        letter_bank_copy = copy.deepcopy(self.letter_bank)

        for letter in word:
            if letter in letter_bank_copy:
                letter_bank_copy.remove(letter)
            else:
                return False
        
        return True
