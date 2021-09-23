import copy
import random
from adagrams.hand import Hand

class Adagrams:
    def __init__(self, letter_pool, letter_values):
        self.letter_pool = letter_pool
        self.letter_values = letter_values
        self.hand = Hand()
        self.word_list = []

    def draw_letters(self):
        letter_pool_copy = copy.deepcopy(self.letter_pool)

        while len(self.hand.letter_bank) < 10:
            letter = random.choice(list(letter_pool_copy.keys()))
            if letter_pool_copy[letter] > 0:
                self.hand.letter_bank.append(letter)
                letter_pool_copy[letter] -= 1

    def score_word(self, word):
        score = 0
        for letter in word:
            score += self.letter_values[letter.upper()]

        if len(word) > 6 and len(word) < 11:
            score += 8

        return score

    def add_valid_word_to_list(self, word):
        if self.hand.uses_available_letters(word):
            self.word_list.append(word)
            print(f"Nice {len(word)} letter word!")
        else:
            print("You can't make that word")


    def get_highest_word_score(self):
        highest = (self.word_list[0],0)
        for word in self.word_list:
            score = self.score_word(word)
            if score > highest[1]:
                highest = (word, score)
            elif score == highest[1]:
                if len(highest[0]) == 10:
                    pass
                elif len(word) == 10 and len(highest[0]) != 10:
                    highest = (word, score)
                elif len(word) < len(highest[0]):
                    highest = (word, score)

        return highest