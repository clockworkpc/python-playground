import pytest
from code.module4_two_pointers import Module4

def test_has_pair_with_sum():
    assert Module4.has_pair_with_sum([1, 2, 4, 4], 8) == True

def test_remove_duplicates():
    assert Module4.remove_duplicates([1, 1, 2]) == [1, 2]

def test_two_sum_indices():
    assert Module4.two_sum_indices([2, 7, 11, 15], 9) == [0, 1]

def test_move_zeroes():
    assert Module4.move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]

def test_reverse_string():
    assert Module4.reverse_string(['h', 'e', 'l', 'l', 'o']) == ['o', 'l', 'l', 'e', 'h']
