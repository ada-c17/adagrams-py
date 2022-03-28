import sys
import random
import string
from adagrams.ui_helper import *
from adagrams.game import draw_letters, uses_available_letters, score_word, get_highest_word_score
letters_dict = {
    "A": 9,
    "B": 2,
    "C": 2,
    "D": 4,
    "E": 12,
    "F": 2,
    "G": 3,
    "H": 2,
    "I": 9,
    "J": 1,
    "K": 1,
    "L": 4,
    "M": 2,
    "N": 6,
    "O": 8,
    "P": 2,
    "Q": 1,
    "R": 6,
    "S": 4,
    "T": 6,
    "U": 4,
    "V": 2,
    "W": 2,
    "X": 1,
    "Y": 2,
    "Z": 1
}

def draw_letters():
    """
    output: list of 10 strings
    no parameters
    letters should be randomly drawn from a pool of letters
    letters should reflect distribution from a table
    (dictionary, pool_of_letters)
    drawn letters cannot return more than the allotted amount(?)
    once something is drawn, will probably have to subtract from the value of that letter by 1
    if the value is 0, make it no longer accessible
    possibly make list of dicts if random doesnt work?
    random.choice()?

    """
    hand_list = []
    hand_dict = letters_dict.copy()
    for i in range(10):
        random_letter = random.choice(string.ascii_uppercase)
        for letter in hand_dict:
            if letter == random_letter:
                if hand_dict[letter] >= 1:
                    hand_list.append(letter)
                    hand_dict[letter] -= 1 
    # print(", ".join(hand_list))  
    return hand_list
def wave_1_run_game():
    display_welcome_message()
    game_continue = True
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
    
        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input == "y"
   
    display_goodbye_message()

def wave_2_run_game():
    display_welcome_message()
    game_continue = True
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
        display_game_instructions()
        user_input_word = input()

        while( not uses_available_letters(user_input_word, letter_bank)):
            display_needs_valid_input_message()
            user_input_word = input()

        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input == "y"
   
    display_goodbye_message()

def wave_3_run_game():
    display_welcome_message()
    game_continue = True
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
        display_game_instructions()
        user_input_word = input()

        while( not uses_available_letters(user_input_word, letter_bank)):
            display_needs_valid_input_message()
            user_input_word = input()
        
        score = score_word(user_input_word)
        display_score(score)

        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input == "y"
    display_goodbye_message()

def wave_4_run_game():
    display_welcome_message()
    game_continue = True
    played_words = []
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
        display_game_instructions()
        user_input_word = input()

        while( not uses_available_letters(user_input_word, letter_bank)):
            display_needs_valid_input_message()
            user_input_word = input()
        
        score = score_word(user_input_word)
        display_score(score)
        played_words.append(user_input_word)

        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input == "y"
    display_highest_score(get_highest_word_score(played_words))
    display_goodbye_message()

def main(wave):
    if(wave == 1):
        wave_1_run_game()
    elif(wave == 2):
        wave_2_run_game()
    elif(wave == 3):
        wave_3_run_game()
    elif(wave == 4):
        wave_4_run_game()
    else:
        print("Please input a wave number.  Valid wave numbers are 1, 2, 3, 4.")

if __name__ == "__main__":
    args = sys.argv
    if(len(args) >= 2 and args[1].isnumeric()):
        wave = int(args[1])
    else:
        wave = "ERROR"
    main(wave)