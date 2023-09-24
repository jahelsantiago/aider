import unittest
from aider.utils import word_distance



def test_word_distance_empty():
    assert word_distance("", "") == 0
    assert word_distance("", "a") == 1
    assert word_distance("a", "") == 1

def test_word_distance_equal():
    assert word_distance("abc", "abc") == 0
    assert word_distance("a", "a") == 0

def test_word_distance_insert():
    assert word_distance("a", "ab") == 1
    assert word_distance("a", "abc") == 2
    assert word_distance("ab", "abc") == 1
    assert word_distance("abc", "abcd") == 1
    assert word_distance("abcd", "abcde") == 1

def test_word_distance_long_word():
    assert word_distance("pneumonoultramicroscopicsilicovolcanoconiosis", "floccinaucinihilipilification") == 34
    