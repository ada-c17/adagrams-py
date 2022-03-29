import pytest

from adagrams.game import score_word

def test_score_word_accurate():
    #Arrange
    word_1 = "A"
    word_2 = "DOG"
    word_3 = "WHIMSY"
    #Act
    score_1 = score_word(word_1)
    score_2 = score_word(word_2)
    score_3 = score_word(word_3)
    
    # Assert
    assert score_1 == 1
    assert score_2 == 5
    assert score_3 == 17

def test_score_word_accurate_ignores_case():
    #Arrange
    word_1 = "a"
    word_2 = "dog"
    word_3 = "wHiMsY"
    #Act
    score_1 = score_word(word_1)
    score_2 = score_word(word_2)
    score_3 = score_word(word_3)
    # Assert
    assert score_1 == 1
    assert score_2 == 5
    assert score_3 == 17

def test_score_zero_for_empty():
    #Arrange
    word_1 = ""
    
    #Act 
    score_1 = score_word(word_1)

    # Assert
    assert score_1 == 0

def test_score_extra_points_for_seven_or_longer():
    #Arrange
    word_1 = "XXXXXXX"
    word_2 = "XXXXXXXX"
    word_3 = "XXXXXXXXX"

    #Act
    score_1 = score_word(word_1)
    score_2 = score_word(word_2)
    score_3 = score_word(word_3)

    # Assert
    assert score_1== 64
    assert score_2 == 72
    assert score_3 == 80
    