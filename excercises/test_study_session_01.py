import pytest
from excercises.day_01_functions_01 import is_even, percentage, clamp_score, classify_mastery

@pytest.mark.parametrize("a,expected", [
    (2, True),
    (3, False), 
    (0, True),
])

def test_is_even(a, expected):
    assert is_even(a) == expected

@pytest.mark.parametrize("a,b,expected", [
    (1, 4, 25.0),
    (0, 100, 0),
    (5, 0, ValueError),
])

def test_percentage(a, b, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            percentage(a, b)
    else:
        assert percentage(a, b) == expected


@pytest.mark.parametrize("a,expected", [
    (-4,  0),
    (70,  70),
    (104, 100),
])

def test_clamp_score(a, expected):
    assert clamp_score(a) == expected


@pytest.mark.parametrize("a,expected", [
    (0,  "unknown"),
    (39,  "unknown"),
    (40, "developing"),
    (69,  "developing"),
    (70,  "proficient"),
    (89, "proficient"),
    (90, "advanced"),
    (100,  "advanced"),
    (120,  "advanced"),
    (-7, "unknown"),
])

def test_classify_mastery(a, expected):
    assert classify_mastery(a) == expected
