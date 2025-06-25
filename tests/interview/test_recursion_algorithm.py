
import pytest
from code.interview.recursion_algorithm import RecursionAlgorithm

# Tower of Hanoi
def test_tower_of_hanoi_case1():
    assert RecursionAlgorithm.tower_of_hanoi(1) == 1

def test_tower_of_hanoi_case2():
    assert RecursionAlgorithm.tower_of_hanoi(2) == 3

def test_tower_of_hanoi_case3():
    assert RecursionAlgorithm.tower_of_hanoi(3) == 7

def test_tower_of_hanoi_case4():
    assert RecursionAlgorithm.tower_of_hanoi(4) == 15

def test_tower_of_hanoi_case5():
    assert RecursionAlgorithm.tower_of_hanoi(5) == 31
