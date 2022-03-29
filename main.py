import sys
from adagrams.ui_helper import *
from adagrams.game import draw_letters, uses_available_letters, score_word, get_highest_word_score

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

LETTER_SCORES = {
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
    'P': 3, 
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

def wave_1_run_game():
    display_welcome_message()
    game_continue = True
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters(LETTER_POOL)
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
        letter_bank = draw_letters(LETTER_POOL)
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