import pytest
from code.module3_subtasks import Module3

def test_sum_range():
    assert Module3.sum_range(1, 5) == 15

def test_fibonacci():
    assert Module3.fibonacci(5) == 5

def test_factorial():
    assert Module3.factorial(4) == 24

def test_gcd():
    assert Module3.gcd(12, 18) == 6

def test_lcm():
    assert Module3.lcm(4, 5) == 20
