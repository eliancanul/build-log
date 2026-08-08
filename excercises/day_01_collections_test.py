from excercises.day_01_collections import count_correct_attempts, attempts, concepts_attempted, independent_attempts
import pytest


def test_count_correct_attempts():
    result = count_correct_attempts(attempts)
    assert result == 1

def test_count_correct_attempts_empty_list():
    result = count_correct_attempts([])
    assert result == 0

def test_concepts_attemted():
    result = concepts_attempted(attempts)
    assert result == {'functions', 'testing'}

def test_concepts_attemted_empty_list():
    result = concepts_attempted([])
    assert result == set()

def test_independent_attempts():
    result = independent_attempts(attempts)
    assert result == [{
        "concept": "functions",
        "correct": True,
        "assistance": 0,
   }]
def test_independent_attempts_empty_list():
    result = independent_attempts([])
    assert result == []