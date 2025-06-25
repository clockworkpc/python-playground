
import pytest
from code.interview.bit_manipulation_algorithm import BitManipulationAlgorithm

# Find the Single Number
def test_single_number_case1():
    assert BitManipulationAlgorithm.single_number([2,2,1]) == 1

def test_single_number_case2():
    assert BitManipulationAlgorithm.single_number([4,1,2,1,2]) == 4

def test_single_number_case3():
    assert BitManipulationAlgorithm.single_number([1]) == 1

def test_single_number_case4():
    assert BitManipulationAlgorithm.single_number([1,2,2]) == 1

def test_single_number_case5():
    assert BitManipulationAlgorithm.single_number([300,300,400]) == 400
