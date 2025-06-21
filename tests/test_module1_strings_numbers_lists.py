import pytest
from code.module1.module1 import Module1


# String tests
def test_string_concatenation():
    assert Module1.concatenate_strings('Hello', 'World') == "Hello World"

def test_string_upper():
    assert Module1.uppercase('hello') == "HELLO"

def test_string_strip():
    assert Module1.strip_whitespace("  hello  ") == "hello"

def test_string_find():
    assert Module1.find_substring("banana", "na") == 2

def test_string_replace():
    assert Module1.replace_substring("hello world", "world", "there") == "hello there"

# Number tests
def test_integer_addition():
    assert Module1.add(2, 3) == 5

def test_integer_division():
    assert Module1.divide(10, 2) == 5.0

def test_integer_modulus():
    assert Module1.modulus(10, 3) == 1

def test_float_precision():
    result = Module1.add_floats(0.1, 0.2)
    assert round(result, 1) == 0.3

def test_exponentiation():
    assert Module1.power(2, 3) == 8

# List tests
def test_list_append():
    assert Module1.append_to_list([1, 2, 3], 4) == [1, 2, 3, 4]

def test_list_extend():
    assert Module1.extend_list([1, 2], [3, 4]) == [1, 2, 3, 4]

def test_list_pop():
    assert Module1.pop_from_list([1, 2, 3]) == 3

def test_list_remove():
    assert Module1.remove_from_list([1, 2, 3], 2) == [1, 3]

def test_list_sort():
    assert Module1.sort_list([3, 1, 2]) == [1, 2, 3]

def test_list_reverse():
    assert Module1.reverse_list([1, 2, 3]) == [3, 2, 1]

def test_list_index():
    assert Module1.index_of_element(['a', 'b', 'c'], 'b') == 1

def test_list_slice():
    assert Module1.slice_list([0, 1, 2, 3, 4], 1, 4) == [1, 2, 3]

def test_list_comprehension():
    assert Module1.double_elements([1, 2, 3]) == [2, 4, 6]

def test_list_sum():
    assert Module1.sum_list([1, 2, 3, 4]) == 10
