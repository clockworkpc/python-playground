# type: ignore[arg-type]

from code.module3.subtasks import Subtasks
import pytest

def test_filter_and_double_normal():
    assert Subtasks.process_and_filter([1, 2, 3, 4]) == [4, 8]

def test_filter_and_double_empty():
    assert Subtasks.process_and_filter([]) == []

def test_filter_and_double_no_even():
    assert Subtasks.process_and_filter([1, 3, 5]) == []

def test_filter_and_double_all_even():
    assert Subtasks.process_and_filter([2, 4]) == [4, 8]

def test_filter_and_double_negative_even():
    assert Subtasks.process_and_filter([-2, -4]) == [-4, -8]
