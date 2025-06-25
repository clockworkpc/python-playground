
import pytest
from code.interview.sorting_algorithm import SortingAlgorithm

# Quick Sort
def test_quick_sort_case1():
    assert SortingAlgorithm.quick_sort([3,6,8,10,1,2,1]) == sorted([3,6,8,10,1,2,1])

def test_quick_sort_case2():
    assert SortingAlgorithm.quick_sort([1]) == [1]

def test_quick_sort_case3():
    assert SortingAlgorithm.quick_sort([]) == []

def test_quick_sort_case4():
    assert SortingAlgorithm.quick_sort([5,4,3,2,1]) == [1,2,3,4,5]

def test_quick_sort_case5():
    assert SortingAlgorithm.quick_sort([1,3,9,8,2,7,5]) == sorted([1,3,9,8,2,7,5])

# Merge Sort
def test_merge_sort_case1():
    assert SortingAlgorithm.merge_sort([38,27,43,3,9,82,10]) == sorted([38,27,43,3,9,82,10])

def test_merge_sort_case2():
    assert SortingAlgorithm.merge_sort([1]) == [1]

def test_merge_sort_case3():
    assert SortingAlgorithm.merge_sort([]) == []

def test_merge_sort_case4():
    assert SortingAlgorithm.merge_sort([5,4,3,2,1]) == [1,2,3,4,5]

def test_merge_sort_case5():
    assert SortingAlgorithm.merge_sort([10,7,8,9,1,5]) == sorted([10,7,8,9,1,5])
