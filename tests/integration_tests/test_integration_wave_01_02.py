import pytest
import copy

from adagrams.game import draw_letters, uses_available_letters

@pytest.mark.integration_test
def test_complete_game():

    # draw_letters
    letters = draw_letters()

    assert len(letters) == 10

    for elem in letters:
        assert type(elem) == str
        assert len(elem) == 1

    # letter_bank
    letter_bank = copy.deepcopy(letters)
    false_word = 10*letter_bank[0]
    true_word = letter_bank.join("")

    assert uses_available_letters(false_word, letter_bank) == False
    assert uses_available_letters(true_word, letter_bank) == True

