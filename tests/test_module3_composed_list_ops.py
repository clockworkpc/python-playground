# type: ignore[arg-type]

from code.module3.composed_list_ops import ComposedListOps
import pytest

def test_filter_and_double_normal():
    assert ComposedListOps.process_and_filter([1, 2, 3, 4]) == [4, 8]
#
def test_filter_and_double_empty():
    assert ComposedListOps.process_and_filter([]) == []

def test_filter_and_double_no_even():
    assert ComposedListOps.process_and_filter([1, 3, 5]) == []

def test_filter_and_double_all_even():
    assert ComposedListOps.process_and_filter([2, 4]) == [4, 8]

def test_filter_and_double_negative_even():
    assert ComposedListOps.process_and_filter([-2, -4]) == [-4, -8]

def test_evens_squared_basic():
    assert ComposedListOps.filter_and_square_evens([1, 2, 3, 4]) == [4, 16]

def test_evens_squared_none():
    assert ComposedListOps.filter_and_square_evens([1, 3, 5]) == []

def test_evens_squared_all():
    assert ComposedListOps.filter_and_square_evens([2, 4]) == [4, 16]

def test_evens_squared_negative():
    assert ComposedListOps.filter_and_square_evens([-2, -3, -4]) == [4, 16]

def test_evens_squared_empty():
    assert ComposedListOps.filter_and_square_evens([]) == []
