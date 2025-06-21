import pytest
from code.module3.subtasks import Subtask


def test_sum_range():
    assert Subtask.sum_range(1, 5) == 15


def test_fibonacci():
    assert Subtask.fibonacci(5) == 5


def test_factorial():
    assert Subtask.factorial(4) == 24


def test_gcd():
    assert Subtask.greatest_common_divisor(12, 18) == 6


def test_lcm():
    assert Subtask.least_common_multiple(4, 5) == 20
