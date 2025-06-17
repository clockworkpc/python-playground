# type: ignore[arg-type]

from code.module1.array_ops import ArrayOps
import pytest

def test_array_doubler():
    assert ArrayOps.array_doubler([1, 2, 3]) == [2, 4, 6]
    assert ArrayOps.array_doubler([]) == []
    with pytest.raises(TypeError): ArrayOps.array_doubler(['a', 'b', 'c'])

def test_even_filter():
    assert ArrayOps.even_filter([1, 2, 3, 4]) == [2, 4]
    assert ArrayOps.even_filter([]) == []
    with pytest.raises(TypeError): ArrayOps.even_filter(['a', 'b', 'c'])

def test_every_other_element():
    assert ArrayOps.every_other_element([5, 6, 7, 8, 9]) == [5, 7, 9]
    assert ArrayOps.every_other_element([]) == []
    with pytest.raises(TypeError): ArrayOps.every_other_element(['a', 'b', 'c'])
#
def test_last_digit_extractor():
    assert ArrayOps.last_digit_extractor([123, 456, 789]) == [3, 6, 9]

def test_index_parity_mask():
    assert ArrayOps.index_parity_mask([1, 2, 3, 4]) == [-1, 2, -3, 4]
