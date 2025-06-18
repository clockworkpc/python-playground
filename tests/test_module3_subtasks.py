# type: ignore[arg-type]

from code.module3.arrays import Arrays
import pytest

def test_filter():
    assert Arrays.filter_evens([1,2,3,4]) == [2, 4]

def double_normal():
    assert Arrays.double_normal([2, 4]) == [4, 8]

def test_filter_and_double_normal():
    assert Arrays.process_and_filter([1, 2, 3, 4]) == [4, 8]
#
def test_filter_and_double_empty():
    assert Arrays.process_and_filter([]) == []

def test_filter_and_double_no_even():
    assert Arrays.process_and_filter([1, 3, 5]) == []

def test_filter_and_double_all_even():
    assert Arrays.process_and_filter([2, 4]) == [4, 8]

def test_filter_and_double_negative_even():
    assert Arrays.process_and_filter([-2, -4]) == [-4, -8]

def test_evens_squared_basic():
    assert Arrays.filter_and_square_evens([1, 2, 3, 4]) == [4, 16]

def test_evens_squared_none():
    assert Arrays.filter_and_square_evens([1, 3, 5]) == []

def test_evens_squared_all():
    assert Arrays.filter_and_square_evens([2, 4]) == [4, 16]

def test_evens_squared_negative():
    assert Arrays.filter_and_square_evens([-2, -3, -4]) == [4, 16]

def test_evens_squared_empty():
    assert Arrays.filter_and_square_evens([]) == []
