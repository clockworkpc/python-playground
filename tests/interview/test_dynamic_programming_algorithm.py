
import pytest
from code.interview.dynamic_programming_algorithm import DynamicProgrammingAlgorithm

# Longest Increasing Subsequence
def test_lis_case1():
    assert DynamicProgrammingAlgorithm.lis([10,9,2,5,3,7,101,18]) == 4

def test_lis_case2():
    assert DynamicProgrammingAlgorithm.lis([0,1,0,3,2,3]) == 4

def test_lis_case3():
    assert DynamicProgrammingAlgorithm.lis([7,7,7,7,7,7,7]) == 1

def test_lis_case4():
    assert DynamicProgrammingAlgorithm.lis([4,10,4,3,8,9]) == 3

def test_lis_case5():
    assert DynamicProgrammingAlgorithm.lis([1,3,6,7,9,4,10,5,6]) == 6
