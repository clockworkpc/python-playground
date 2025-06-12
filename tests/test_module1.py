import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module1 import *
import pytest

# 🔢 Basic Operations with Numbers

def test_increment_by_index():
    assert increment_by_index([5, 10, 15]) == [5, 11, 17]
    assert increment_by_index([]) == []
    assert increment_by_index(['a', 'b', 'c']) == []

def test_modulo_alternator():
    assert modulo_alternator([4, 7, 2, 9]) == [0, 1, 0, 1]
    assert modulo_alternator([]) == []
    assert modulo_alternator(['a', 'b', 'c']) == []

def test_running_total():
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_total([]) == []
    assert running_total(['a', 'b', 'c']) == []

def test_double_negatives():
    assert double_negatives([-2, 3, -1, 5]) == [-4, 3, -2, 5]
    assert double_negatives([]) == []
    assert double_negatives(['a', 'b', 'c']) == []

def test_absolute_shift():
    assert absolute_shift([3, -4, 2]) == [3, -1, 6]
    assert absolute_shift([]) == []
    assert absolute_shift(['a', 'b', 'c']) == []

# 🔤 Basic String Manipulation

# def test_vowel_remover():
#     assert vowel_remover("education") == "dctn"
#
# def test_reverse_words():
#     assert reverse_words("hello world") == "world hello"
#
# def test_initials_extractor():
#     assert initials_extractor("John Ronald Reuel Tolkien") == "JRRT"
#
# def test_duplicate_separator():
#     assert duplicate_separator("abc") == "aabbcc"
#
# def test_title_casing():
#     assert title_casing("this is a test") == "This Is A Test"
#
# # 🧮 Basic Array Manipulation
#
# def test_array_doubler():
#     assert array_doubler([1, 2, 3]) == [2, 4, 6]
#
# def test_even_filter():
#     assert even_filter([1, 2, 3, 4]) == [2, 4]
#
# def test_every_other_element():
#     assert every_other_element([5, 6, 7, 8, 9]) == [5, 7, 9]
#
# def test_last_digit_extractor():
#     assert last_digit_extractor([123, 456, 789]) == [3, 6, 9]
#
# def test_index_parity_mask():
#     assert index_parity_mask([1, 2, 3, 4]) == [-1, 2, -3, 4]
