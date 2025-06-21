import pytest
from code.module2.module2 import Module2

def test_repeat_string():
    assert Module2.repeat_string('abc', 3) == 'abcabcabc'

def test_is_palindrome():
    assert Module2.is_palindrome('racecar') == True

def test_string_length():
    assert Module2.string_length('hello') == 5

def test_capitalize_words():
    assert Module2.capitalize_words('hello world') == 'Hello World'

def test_join_with_dash():
    assert Module2.join_with_dash(['a', 'b', 'c']) == 'a-b-c'

def test_multiply():
    assert Module2.multiply(4, 5) == 20

def test_is_even():
    assert Module2.is_even(4) == True

def test_floor_divide():
    assert Module2.floor_divide(7, 2) == 3
#
def test_round_to_int():
    assert Module2.round_to_int(3.7) == 4

def test_abs_value():
    assert Module2.abs_value(-10) == 10

def test_merge_lists():
    assert Module2.merge_lists([1], [2, 3]) == [1, 2, 3]

def test_list_difference():
    assert Module2.list_difference([1, 2], [2]) == [1]

def test_list_intersection():
    assert Module2.list_intersection([1, 2], [2, 3]) == [2]

def test_list_max():
    assert Module2.list_max([1, 2, 3]) == 3

def test_list_min():
    assert Module2.list_min([1, 2, 3]) == 1

def test_unique_elements():
    assert Module2.unique_elements([1, 1, 2]) == [1, 2]

def test_filter_even():
    assert Module2.filter_even([1, 2, 3, 4]) == [2, 4]

def test_count_occurrences():
    assert Module2.count_occurrences([1, 1, 1], 1) == 3

def test_list_to_string():
    assert Module2.list_to_string([1, 2, 3]) == '1,2,3'

def test_list_length():
    assert Module2.list_length([1, 2, 3]) == 3
