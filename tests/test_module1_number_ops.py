# type: ignore[arg-type]

from module1.number_ops import NumberOps
import pytest

def test_increment_by_index():
    assert NumberOps.increment_by_index([5, 10, 15]) == [5, 11, 17]
    assert NumberOps.increment_by_index([]) == []
    with pytest.raises(TypeError): NumberOps.increment_by_index(['a', 'b', 'c'])
    with pytest.raises(TypeError): NumberOps.increment_by_index('hello')

def test_modulo_alternator():
    assert NumberOps.modulo_alternator([4, 7, 2, 9]) == [0, 1, 0, 1]
    assert NumberOps.modulo_alternator([]) == []
    with pytest.raises(TypeError): NumberOps.modulo_alternator(['a', 'b', 'c'])
    with pytest.raises(TypeError): NumberOps.modulo_alternator('hello')

def test_running_total():
    assert NumberOps.running_total([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert NumberOps.running_total([]) == []
    with pytest.raises(TypeError): NumberOps.running_total(['a', 'b', 'c'])
    with pytest.raises(TypeError): NumberOps.running_total('hello')

def test_double_negatives():
    assert NumberOps.double_negatives([-2, 3, -1, 5]) == [-4, 3, -2, 5]
    assert NumberOps.double_negatives([]) == []
    with pytest.raises(TypeError): NumberOps.double_negatives(['a', 'b', 'c'])
    with pytest.raises(TypeError): NumberOps.double_negatives('hello')

def test_absolute_shift():
    assert NumberOps.absolute_shift([3, -4, 2]) == [3, -1, 6]
    assert NumberOps.absolute_shift([]) == []
    with pytest.raises(TypeError): NumberOps.absolute_shift(['a', 'b', 'c'])
    with pytest.raises(TypeError): NumberOps.absolute_shift('hello')

