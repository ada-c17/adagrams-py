import pytest

from adagrams.game import score_word

'''
  # Arrange
    letters = ["D", "O", "G", "X", "X", "X", "X", "X", "X", "X"]
    word = "DOG"

    # Act
    is_valid = uses_available_letters(word, letters)

    # Assert
    assert is_valid == True
'''


def test_score_word_accurate():
    # Arrange
    word_list = ["A", "DOG", "WHYMSY"]

    # Act/Assert
    assert score_word(word_list[0]) == 1
    assert score_word(word_list[1]) == 5
    assert score_word(word_list[2]) == 20

def test_score_word_accurate_ignores_case():
    # Arrange
    word_list = ["a", "dog", "whimsy"]

    # Act/Assert
    assert score_word(word_list[0]) == 1
    assert score_word(word_list[1]) == 5
    assert score_word(word_list[2]) == 17

def test_score_zero_for_empty():
    # Arrange
    word = ""

    # Act/Assert
    assert score_word(word) == 0

def test_score_extra_points_for_seven_or_longer():
    # Arrange
    word_list = ["XXXXXXX", "XXXXXXXX", "XXXXXXXXX"]

    # Act/Assert
    assert score_word(word_list[0]) == 64
    assert score_word(word_list[1]) == 72
    assert score_word(word_list[2]) == 80
