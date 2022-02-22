import pytest

from adagrams.game import score_word,get_highest_word_score

@pytest.mark.integration_test
def test_wave_03_04():

    # clear winner
    words = ["XXXX", "X", "XX", "XXX"]

    # Act
    best_word = get_highest_word_score(words)
    # NOTE: best_word can be a tuple or a list

    # Assert
    assert best_word[0] == "XXXX"
    assert best_word[1] == 32
