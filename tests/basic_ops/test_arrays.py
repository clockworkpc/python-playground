# type: ignore[arg-type]

from basic_ops.arrays import Arrays
import pytest

def test_array_doubler():
    assert Arrays.array_doubler([1, 2, 3]) == [2, 4, 6]
    assert Arrays.array_doubler([]) == []
    with pytest.raises(TypeError): Arrays.array_doubler(['a', 'b', 'c'])

def test_even_filter():
    assert Arrays.even_filter([1, 2, 3, 4]) == [2, 4]
    assert Arrays.even_filter([]) == []
    with pytest.raises(TypeError): Arrays.even_filter(['a', 'b', 'c'])

def test_every_other_element():
    assert Arrays.every_other_element([5, 6, 7, 8, 9]) == [5, 7, 9]
    assert Arrays.every_other_element([]) == []
    with pytest.raises(TypeError): Arrays.every_other_element(['a', 'b', 'c'])
#
def test_last_digit_extractor():
    assert Arrays.last_digit_extractor([123, 456, 789]) == [3, 6, 9]

def test_index_parity_mask():
    assert Arrays.index_parity_mask([1, 2, 3, 4]) == [-1, 2, -3, 4]
