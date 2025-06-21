import pytest
from code.module3_multidimensional_arrays import Module3

def test_iterate_nested_array_1():
    assert Module3.iterate_nested_array_1([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_iterate_nested_array_2():
    assert Module3.iterate_nested_array_2([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_iterate_nested_array_3():
    assert Module3.iterate_nested_array_3([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_iterate_nested_array_4():
    assert Module3.iterate_nested_array_4([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_iterate_nested_array_5():
    assert Module3.iterate_nested_array_5([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_transpose_matrix_1():
    assert Module3.transpose_matrix_1([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_transpose_matrix_2():
    assert Module3.transpose_matrix_2([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_transpose_matrix_3():
    assert Module3.transpose_matrix_3([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_transpose_matrix_4():
    assert Module3.transpose_matrix_4([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_transpose_matrix_5():
    assert Module3.transpose_matrix_5([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
