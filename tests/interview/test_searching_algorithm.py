
import pytest
from code.interview.searching_algorithm import SearchingAlgorithm

# Binary Search
def test_binary_search_case1():
    assert SearchingAlgorithm.binary_search([1,2,3,4,5], 3) == 2

def test_binary_search_case2():
    assert SearchingAlgorithm.binary_search([1,2,3,4,5], 1) == 0

def test_binary_search_case3():
    assert SearchingAlgorithm.binary_search([1,2,3,4,5], 5) == 4

def test_binary_search_case4():
    assert SearchingAlgorithm.binary_search([1,3,5,7,9], 6) == -1

def test_binary_search_case5():
    assert SearchingAlgorithm.binary_search([], 1) == -1
