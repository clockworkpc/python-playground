# type: ignore[arg-type]

from code.module2.array_ops import ArrayOps
import pytest

def test_double_basic():
    assert ArrayOps.double_array([1, 2, 3]) == [2, 4, 6]

def test_double_negative():
    assert ArrayOps.double_array([-1, -2]) == [-2, -4]

def test_double_zero():
    assert ArrayOps.double_array([0]) == [0]

def test_double_empty():
    assert ArrayOps.double_array([]) == []

def test_double_large():
    assert ArrayOps.double_array([1000000]) == [2000000]

def test_reverse_integers():
    assert ArrayOps.reverse_array([1, 2, 3]) == [3, 2, 1]

def test_reverse_strings():
    assert ArrayOps.reverse_array(["a", "b", "c"]) == ["c", "b", "a"]

def test_reverse_empty():
    assert ArrayOps.reverse_array([]) == []

def test_reverse_single():
    assert ArrayOps.reverse_array([42]) == [42]

def test_reverse_nested():
    assert ArrayOps.reverse_array([[1], [2]]) == [[2], [1]]

def test_concat_ints():
    assert ArrayOps.concat_arrays([1, 2], [3, 4]) == [1, 2, 3, 4]

def test_concat_strings():
    assert ArrayOps.concat_arrays(["a"], ["b", "c"]) == ["a", "b", "c"]

def test_concat_empty_first():
    assert ArrayOps.concat_arrays([], [1]) == [1]

def test_concat_empty_second():
    assert ArrayOps.concat_arrays([1], []) == [1]

def test_concat_both_empty():
    assert ArrayOps.concat_arrays([], []) == []

def test_concat_string_and_int_mixed():
    assert ArrayOps.concat_arrays(["a", "b"], [1, 2])
