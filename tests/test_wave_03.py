import pytest

from adagrams.game import score_word
score_dict = {  'A' : 1, 'E' : 1, 'I' : 1, 'O' : 1, 'U' : 1, 'L' : 1, 'N' : 1, 'R' : 1, 'S' : 1, 'T' : 1,
                'D' : 2, 'G' : 2,
                'B' : 3, 'C' : 3, 'M' : 3, 'P' : 3,
                'F' : 4, 'H' : 4, 'V' : 4, 'W' : 4, 'Y' : 4,
                'K' : 5,
                'J' : 8, 'X' : 8,
                'Q' : 10, 'Z' : 10}

def test_score_word_accurate():
    #Arrange
    WORD_1 = "A"
    WORD_2 = "DOG"
    WORD_3 = "WHIMSY"
    #Act
    result_1 = score_word(WORD_1)
    result_2 = score_word(WORD_2)
    result_3 = score_word(WORD_3)

    # Assert
    assert result_1 == 1
    assert result_2 == 5
    assert result_3 == 17

def test_score_word_accurate_ignores_case():
    # Arrange
    WORD_1 = "a"
    WORD_2 = "dog"
    WORD_3 = "wHiMsY"
        #Act
    result_1 = score_word(WORD_1)
    result_2 = score_word(WORD_2)
    result_3 = score_word(WORD_3)

    # Assert
    assert result_1 == 1
    assert result_2 == 5
    assert result_3 == 17

def test_score_zero_for_empty():
    #Arrange
    EMPTY_WORD = ""
    #Act
    result = score_word(EMPTY_WORD)

    # Assert
    assert result == 0

def test_score_extra_points_for_seven_or_longer():
    #Arrange
    BIG_WORD_1 = "XXXXXXX"
    BIG_WORD_2 = "XXXXXXXX"
    BIG_WORD_3 = "XXXXXXXXX"

    #Act
    result_1 = score_word(BIG_WORD_1)
    result_2 = score_word(BIG_WORD_2)
    result_3 = score_word(BIG_WORD_3)

    # Assert
    assert result_1 == 64
    assert result_2 == 72
    assert result_3 == 80
    