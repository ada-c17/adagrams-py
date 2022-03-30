import pytest

from adagrams.game import score_word

def test_score_word_accurate():
    # Arrange 
    word_1 = "A"
    word_2 = "DOG"
    word_3 = "WHIMSY"

    # Act
    result_1 = score_word(word_1)
    result_2 = score_word(word_2)
    result_3 = score_word(word_3)

    # Assert
    assert result_1 == 1
    assert result_2 == 5
    assert result_3 == 17

def test_score_word_accurate_ignores_case():
    # Arrange 
    word_1 = "a"
    word_2 = "dog"
    word_3 = "wHiMsY"

    # Act
    result_1 = score_word(word_1)
    result_2 = score_word(word_2)
    result_3 = score_word(word_3)

    # Assert
    assert result_1 == 1
    assert result_2 == 5
    assert result_3 == 17

def test_score_zero_for_empty():
    # Arrange 
    word = ""

    # Act
    result = score_word(word)

    # Assert
    assert result == 0

def test_score_extra_points_for_seven_or_longer():
    # Arrange 
    word_1 = "XXXXXXX"
    word_2 = "XXXXXXXX"
    word_3 = "XXXXXXXXX"

    # Act
    result_1 = score_word(word_1)
    result_2 = score_word(word_2)
    result_3 = score_word(word_3)

    # Assert
    assert result_1 == 64
    assert result_2 == 72
    assert result_3 == 80
    

def test_all_same_letters():
    # arrange 
    word= "BBBBBB"
    # Act
    result = score_word(word)

    # Assert
    assert result == 18