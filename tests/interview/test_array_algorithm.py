import pytest
from code.interview.array_algorithm import ArrayAlgorithm


# Maximum Subarray Sum (Kadane’s Algorithm)
def test_maximum_subarray_sum_case1():
    assert ArrayAlgorithm.maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_maximum_subarray_sum_case2():
    assert ArrayAlgorithm.maximum_subarray_sum([1, 2, 3, 4, 5]) == 15


def test_maximum_subarray_sum_case3():
    assert ArrayAlgorithm.maximum_subarray_sum([-5, -4, -3, -2, -1]) == -1


def test_maximum_subarray_sum_case4():
    assert ArrayAlgorithm.maximum_subarray_sum([5, -1, 2, -1, 3, -2, 3]) == 11


def test_maximum_subarray_sum_case5():
    assert (
        ArrayAlgorithm.maximum_subarray_sum([100, -90, 50, -40, 30, -20, 10, -5]) == 100
    )


# Find Missing Number
def test_find_missing_number_case1():
    assert ArrayAlgorithm.find_missing_number([1, 2, 4, 5]) == 3


def test_find_missing_number_case2():
    assert ArrayAlgorithm.find_missing_number([2, 3, 1, 5]) == 4


def test_find_missing_number_case3():
    assert ArrayAlgorithm.find_missing_number([1]) == 2


def test_find_missing_number_case4():
    assert ArrayAlgorithm.find_missing_number([1, 2, 3, 4, 6, 7, 8, 9, 10]) == 5


def test_find_missing_number_case5():
    assert (
        ArrayAlgorithm.find_missing_number(list(range(1, 100)) + list(range(101, 102)))
        == 100
    )


# Trapping Rain Water
def test_trapping_rain_water_case1():
    assert ArrayAlgorithm.trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_trapping_rain_water_case2():
    assert ArrayAlgorithm.trapping_rain_water([2, 0, 2]) == 2


def test_trapping_rain_water_case3():
    assert ArrayAlgorithm.trapping_rain_water([3, 0, 0, 2, 0, 4]) == 10


def test_trapping_rain_water_case4():
    assert ArrayAlgorithm.trapping_rain_water([5, 2, 1, 2, 1, 5]) == 14


def test_trapping_rain_water_case5():
    assert ArrayAlgorithm.trapping_rain_water([0, 7, 1, 4, 6]) == 7


# Maximum Product Subarray
def test_maximum_product_subarray_case1():
    assert ArrayAlgorithm.maximum_product_subarray([2, 3, -2, 4]) == 6


def test_maximum_product_subarray_case2():
    assert ArrayAlgorithm.maximum_product_subarray([-2, 0, -1]) == 0


def test_maximum_product_subarray_case3():
    assert ArrayAlgorithm.maximum_product_subarray([-2, 3, -4]) == 24


def test_maximum_product_subarray_case4():
    assert ArrayAlgorithm.maximum_product_subarray([1, 2, 3, 4]) == 24


def test_maximum_product_subarray_case5():
    assert ArrayAlgorithm.maximum_product_subarray([6, -3, -10, 0, 2]) == 180


# Equilibrium Index
def test_equilibrium_index_case1():
    assert ArrayAlgorithm.equilibrium_index([-7, 1, 5, 2, -4, 3, 0]) == 3


def test_equilibrium_index_case2():
    assert ArrayAlgorithm.equilibrium_index([1, 2, 3]) == -1


def test_equilibrium_index_case3():
    assert ArrayAlgorithm.equilibrium_index([2, 4, 2]) == 1


def test_equilibrium_index_case4():
    assert ArrayAlgorithm.equilibrium_index([0, 0, 0, 0]) == 0


def test_equilibrium_index_case5():
    assert ArrayAlgorithm.equilibrium_index([11, -80, 10, 10, 15, 35, 20]) == 6
