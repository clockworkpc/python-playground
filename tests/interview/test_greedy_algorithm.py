
import pytest
from code.interview.greedy_algorithm import GreedyAlgorithm

# Activity Selection
def test_activity_selection_case1():
    activities = [(1,2),(3,4),(0,6),(5,7),(8,9),(5,9)]
    assert GreedyAlgorithm.activity_selection(activities) == 4

def test_activity_selection_case2():
    assert GreedyAlgorithm.activity_selection([(1,2)]) == 1

def test_activity_selection_case3():
    assert GreedyAlgorithm.activity_selection([(1,10),(2,3),(4,5),(6,7),(8,9)]) == 4

def test_activity_selection_case4():
    assert GreedyAlgorithm.activity_selection([(7,9),(0,10),(10,12),(3,5),(5,8)]) == 3

def test_activity_selection_case5():
    assert GreedyAlgorithm.activity_selection([]) == 0
