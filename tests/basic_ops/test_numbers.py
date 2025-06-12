# type: ignore[arg-type]

from basic_ops.numbers import Numbers
import pytest

def test_increment_by_index():
    assert Numbers.increment_by_index([5, 10, 15]) == [5, 11, 17]
    assert Numbers.increment_by_index([]) == []
    with pytest.raises(TypeError): Numbers.increment_by_index(['a', 'b', 'c'])
    with pytest.raises(TypeError): Numbers.increment_by_index('hello')

def test_modulo_alternator():
    assert Numbers.modulo_alternator([4, 7, 2, 9]) == [0, 1, 0, 1]
    assert Numbers.modulo_alternator([]) == []
    with pytest.raises(TypeError): Numbers.modulo_alternator(['a', 'b', 'c'])
    with pytest.raises(TypeError): Numbers.modulo_alternator('hello')

def test_running_total():
    assert Numbers.running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert Numbers.running_total([]) == []
    with pytest.raises(TypeError): Numbers.running_total(['a', 'b', 'c'])
    with pytest.raises(TypeError): Numbers.running_total('hello')

def test_double_negatives():
    assert Numbers.double_negatives([-2, 3, -1, 5]) == [-4, 3, -2, 5]
    assert Numbers.double_negatives([]) == []
    with pytest.raises(TypeError): Numbers.double_negatives(['a', 'b', 'c'])
    with pytest.raises(TypeError): Numbers.double_negatives('hello')

def test_absolute_shift():
    assert Numbers.absolute_shift([3, -4, 2]) == [3, -1, 6]
    assert Numbers.absolute_shift([]) == []
    with pytest.raises(TypeError): Numbers.absolute_shift(['a', 'b', 'c'])
    with pytest.raises(TypeError): Numbers.absolute_shift('hello')

