# type: ignore[arg-type]

from code.module3.list_ops import ListOps
import pytest

def test_filter():
    assert ListOps.filter_evens([1,2,3,4]) == [2, 4]

def double_normal():
    assert ListOps.double_normal([2, 4]) == [4, 8]

